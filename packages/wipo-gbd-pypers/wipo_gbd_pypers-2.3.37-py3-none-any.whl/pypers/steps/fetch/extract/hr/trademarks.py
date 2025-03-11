import os
import re
import copy 
import requests
from lxml import etree
from pypers.utils import utils
from pypers.steps.base.extract import ExtractBase

class Trademarks(ExtractBase):
    """
    Extract Trademarks archive
    """
    spec = {
        "version": "2.0",
        "descr": [
            "Returns the directory with the extraction"
        ]
    }

    def preprocess(self):
        self.xml_data_map = {"AP": {}, "RE": {}}
        self.data_files = {}
        self.img_files = {}
        self.media_files = {}

        if not len(self.archives):
            return

        extraction_part = self.archives[0]
        archive_file = self.archives[1]
        archive_name = os.path.basename(self.archives[1]).replace(".zip", "")
        # prepare destination dir under pipeline scratch dir
        self.extraction_dir = os.path.join(
            self.meta['pipeline']['output_dir'],
            '__scratch',
            extraction_part,
            archive_name
        )

        # deletes the directory if prev exists
        utils.mkdir_force(self.extraction_dir)

        self.manifest = {'archive_name': archive_name,
                         'archive_file': archive_file,
                         'archive_date': extraction_part,
                         'extraction_dir': self.extraction_dir,
                         'data_files': {},
                         'img_files': {},
                         'media_files': {}}

        # unpack the archives and collect the files
        self.collect_files(self.unpack_archive(archive_file, self.extraction_dir))

    def file_in_archive(self, file, path):
        appnum, ext = os.path.splitext(os.path.basename(file))
        ind = appnum.find("HR")
        appnum = appnum[ind:]
        if ext.lower() == '.xml':
            self.add_xml_file(appnum, os.path.join(path, file))

    def process(self): 
        pass

    def add_xml_file(self, appnum, fullpath):
        # we need to grab URI for applicant, representative and images
        # in each XML file, then inject ApplicantDetails and 
        # RepresentativeDetails fragments in the XML document and save 
        # the XML for the transformation
        proxy_params = self.get_connection_params()
        parser = etree.XMLParser(ns_clean=True, dtd_validation=False, load_dtd=False, no_network=True, recover=True, encoding='utf-8')
        xml_data_rename = fullpath

        root_xml = None
        try:
            parsed_xml = etree.parse(fullpath, parser)
            root_xml = parsed_xml.getroot()
        except Exception as e: 
            self.logger.error("XML parsing failed for %s: %s" % (fullpath, e))
            return

        if root_xml is not None:
            ns = {"tm": "http://www.oami.europa.eu/TM-Search"}
            app_num = root_xml.xpath("//tm:TradeMarkDetails/tm:TradeMark/tm:ApplicationNumber/text()", namespaces=ns)
            if app_num != None and len(app_num)>0:
                app_num = app_num[0]
            if app_num:
                if not app_num[:1].isdigit():
                    app_num = app_num[1:]
                app_num = str(app_num)
            else:
                self.logger.error("Missing application number for %s" % (fullpath))
                return

            app_uri = root_xml.xpath("//tm:ApplicantDetails/tm:Applicant/tm:ApplicantURI/text()", namespaces=ns)
            if not app_uri:
                app_uri = root_xml.xpath("//tm:ApplicantDetails/tm:ApplicantKey/tm:URI/text()", namespaces=ns)
            if app_uri != None and len(app_uri)>0:
                app_uri = app_uri[0]
            if app_uri:
                root_app_xml = None
                # check if the entity is in the local data map, otherwise online look-up
                if app_uri in self.xml_data_map["AP"]:
                    try:
                        root_app_xml = etree.fromstring(bytes(bytearray(self.xml_data_map["AP"][app_uri], encoding='utf-8')), parser)
                    except Exception as e: 
                        self.logger.error("XML parsing failed for %s: %s" % (app_uri, e))
                
                if root_app_xml == None:        
                    try:
                        # retrieve the corresponding XML fragment
                        response = requests.get(app_uri, proxies=proxy_params)
                        if response.ok:
                            self.xml_data_map["AP"][app_uri] = response.text
                            # hack to change the namespace (nothing better with Python apparently)
                            self.xml_data_map["AP"][app_uri] = self.xml_data_map["AP"][app_uri].replace("http://hr.tmview.europa.eu/trademark/applicant", "http://www.oami.europa.eu/TM-Search")
                        else:
                            self.logger.error("XML download failed for %s with code %s" % (app_uri, str(response.status_code)))
                    except Exception as e: 
                        self.logger.error("XML download failed for %s: %s" % (app_uri, e))

                if app_uri in self.xml_data_map["AP"]:
                    try:
                        # parse the fragment
                        root_app_xml = etree.fromstring(bytes(bytearray(self.xml_data_map["AP"][app_uri], encoding='utf-8')), parser)
                    except Exception as e: 
                        self.logger.error("XML parsing failed for %s: %s" % (app_uri, e))

                # inject the fragment
                app_fragment = root_app_xml.xpath("//tm:ApplicantDetails/tm:Applicant", namespaces=ns)
                if app_fragment != None and len(app_fragment)>0:
                    app_fragment = app_fragment[0]

                # complement with applicant URI
                applicant_URI_node = etree.Element("{http://www.oami.europa.eu/TM-Search}ApplicantURI")
                applicant_URI_node.text = app_uri
                app_fragment.insert(0, applicant_URI_node)

                # update the document
                applicant_details_node = root_xml.xpath("//tm:ApplicantDetails", namespaces=ns)
                if applicant_details_node != None and len(applicant_details_node)>0:
                    applicant_details_node = applicant_details_node[0]

                # remove the existing children
                for elem in applicant_details_node:
                    # remove the child
                    applicant_details_node.remove(elem)
                # and replace them with the applicant fragment
                applicant_details_node.insert(0, app_fragment)

                xml_data_rename = os.path.join(os.path.dirname(fullpath), '%s.xml' % app_num)
                with open(xml_data_rename, 'wb') as f:
                    f.write(etree.tostring(parsed_xml, encoding="utf-8", xml_declaration=True, pretty_print=True))
                os.remove(fullpath)

            self.manifest['data_files'].setdefault(app_num, {})
            self.manifest['data_files'][app_num]['ori'] = os.path.relpath(
                xml_data_rename, self.extraction_dir
            )

            img_uri = root_xml.xpath("//tm:MarkImageDetails/tm:MarkImage/tm:MarkImageURI/text()", namespaces=ns)
            if img_uri != None and len(img_uri)>0:
                img_uri = img_uri[0]
            if img_uri:
                self.add_img_url(app_num, img_uri)

