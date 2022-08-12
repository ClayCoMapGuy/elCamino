"""
Model exported as python.
Name : elCamino Tool
Group : 
With QGIS : 32600
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterVectorLayer
from qgis.core import QgsProcessingParameterFeatureSource
from qgis.core import QgsCoordinateReferenceSystem
import processing


class ElcaminoTool(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        # Refers to the address points that Gardner Mayo currently maintains on the Community Development MSSQL Server
        self.addParameter(QgsProcessingParameterVectorLayer('gardners_address_points', "Gardner's Address Points", types=[QgsProcessing.TypeVectorPoint], defaultValue=None))
        # Refers to the Municipalities dataset that Gardner Mayo currently maintains on the Community Development MSSQL Server
        self.addParameter(QgsProcessingParameterFeatureSource('gardners_municipalities', "Gardner's Municipalities", types=[QgsProcessing.TypeVectorPolygon], defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(8, model_feedback)
        results = {}
        outputs = {}

        # Reproject Municipalities
        alg_params = {
            'INPUT': parameters['gardners_municipalities'],
            'OPERATION': '',
            'TARGET_CRS': QgsCoordinateReferenceSystem('EPSG:6447'),
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ReprojectMunicipalities'] = processing.run('native:reprojectlayer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # Reproject APs
        alg_params = {
            'INPUT': parameters['gardners_address_points'],
            'OPERATION': '',
            'TARGET_CRS': QgsCoordinateReferenceSystem('EPSG:6447'),
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ReprojectAps'] = processing.run('native:reprojectlayer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(2)
        if feedback.isCanceled():
            return {}

        # PiP Query
        # This is basically a Point in Polygon Query that: 
        # 1. Picks all the APs that lie within a city boundary;
        # 2. Creates two datasets:
		#	a. APs inside city limits,
		#	b. APs outside city limits;
        # 3. In dataset (a), a new field is given called 'WITHINNAME' that should hold the NAME of the city limits polygon it is WITHIN
		#	note: dataset (b) is just a collection of the APs that are outside cities, this algorithm does nothing else to the data
        alg_params = {
            'DISCARD_NONMATCHING': True,
            'INPUT': outputs['ReprojectAps']['OUTPUT'],
            'JOIN': outputs['ReprojectMunicipalities']['OUTPUT'],
            'JOIN_FIELDS': ['NAME'],
            'METHOD': 0,  # Create separate feature for each matching feature (one-to-many)
            'PREDICATE': [5],  # are within
            'PREFIX': 'WITHIN',
            'NON_MATCHING': QgsProcessing.TEMPORARY_OUTPUT,
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['PipQuery'] = processing.run('native:joinattributesbylocation', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(3)
        if feedback.isCanceled():
            return {}

        # Merge
        # Merges the two datasets from the PiP Query back into a single dataset
        alg_params = {
            'CRS': None,
            'LAYERS': [outputs['PipQuery']['OUTPUT'],outputs['PipQuery']['NON_MATCHING']],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Merge'] = processing.run('native:mergevectorlayers', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(4)
        if feedback.isCanceled():
            return {}

        # Drop field(s)
        # Drops unnecessary fields
        alg_params = {
            'COLUMN': ['OBJECTID','SITEADDID','ADDPTKEY','ESN','OBJECTID','PSAP','MSAG','USNGCOORD','ADDRCLASS','POINTTYPE','CAPTUREMETH','STATUS','LASTUPDATE','LASTEDITOR','created_user','created_date','last_edited_user','last_edited_date','GlobalID','UNIQUEID1','UNIQUE2','PIN_1','URL1','URL2','PIN','LOT','layer','path',''],
            'INPUT': outputs['Merge']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['DropFields'] = processing.run('native:deletecolumn', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(5)
        if feedback.isCanceled():
            return {}

        # Drop M/Z values
        # Drops unnecessary M/Z geometry (must be done for pgSQL)
        alg_params = {
            'DROP_M_VALUES': True,
            'DROP_Z_VALUES': True,
            'INPUT': outputs['DropFields']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['DropMzValues'] = processing.run('native:dropmzvalues', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(6)
        if feedback.isCanceled():
            return {}

        # Add fid
        alg_params = {
            'FIELD_NAME': 'fid',
            'GROUP_FIELDS': [''],
            'INPUT': outputs['DropMzValues']['OUTPUT'],
            'MODULUS': 0,
            'SORT_ASCENDING': True,
            'SORT_EXPRESSION': '',
            'SORT_NULLS_FIRST': False,
            'START': 0,
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['AddFid'] = processing.run('native:addautoincrementalfield', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(7)
        if feedback.isCanceled():
            return {}

        # Export to PostgreSQL
        alg_params = {
            'CREATEINDEX': True,
            'DATABASE': 'doitwebdev01',
            'DROP_STRING_LENGTH': False,
            'ENCODING': 'UTF-8',
            'FORCE_SINGLEPART': False,
            'GEOMETRY_COLUMN': 'geom',
            'INPUT': outputs['AddFid']['OUTPUT'],
            'LOWERCASE_NAMES': True,
            'OVERWRITE': True,
            'PRIMARY_KEY': 'fid',
            'SCHEMA': 'public',
            'TABLENAME': 'addresses'
        }
        outputs['ExportToPostgresql'] = processing.run('native:importintopostgis', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        return results

    def name(self):
        return 'elCamino Tool'

    def displayName(self):
        return 'elCamino Tool'

    def group(self):
        return ''

    def groupId(self):
        return ''

    def createInstance(self):
        return ElcaminoTool()
