# This file was generated by fedex_python.  You probably don't want to edit
# it since your modifications will be lost if fedex_plus is used to
# regenerate it.
import sys

from SCL.SCLBase import *
from SCL.SimpleDataTypes import *
from SCL.ConstructedDataTypes import *
from SCL.AggregationDataTypes import *
from SCL.TypeChecker import check_type
from SCL.Expr import *
from SCL.Builtin import *
from SCL.Rules import *

schema_name = 'test_named_type'

schema_scope = sys.modules[__name__]

measure = REAL
type2 = INTEGER

####################
 # ENTITY line #
####################
class line(BaseEntityClass):
	'''Entity line definition.

	:param line_length
	:type line_length:REAL
	'''
	def __init__( self , line_length, ):
		self.line_length = line_length

	@apply
	def line_length():
		def fget( self ):
			return self._line_length
		def fset( self, value ):
		# Mandatory argument
			if value==None:
				raise AssertionError('Argument line_length is mantatory and can not be set to None')
			if not check_type(value,REAL):
				self._line_length = REAL(value)
			else:
				self._line_length = value
		return property(**locals())
