# Generated from src/grammar/Vsh.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,51,296,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,1,0,5,0,80,
        8,0,10,0,12,0,83,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,93,8,1,
        1,2,1,2,5,2,97,8,2,10,2,12,2,100,9,2,1,2,1,2,5,2,104,8,2,10,2,12,
        2,107,9,2,1,2,1,2,5,2,111,8,2,10,2,12,2,114,9,2,1,2,1,2,5,2,118,
        8,2,10,2,12,2,121,9,2,1,2,3,2,124,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,146,8,
        3,1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,
        9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,11,1,12,1,12,1,12,1,13,1,13,
        1,13,1,14,1,14,1,14,1,15,1,15,1,15,1,16,1,16,1,16,1,17,1,17,1,17,
        1,18,1,18,1,18,1,19,1,19,1,19,1,20,1,20,1,20,1,21,1,21,1,21,1,22,
        1,22,1,22,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,
        1,26,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,
        1,27,1,28,1,28,1,29,1,29,1,29,5,29,235,8,29,10,29,12,29,238,9,29,
        1,29,1,29,5,29,242,8,29,10,29,12,29,245,9,29,1,29,3,29,248,8,29,
        1,30,1,30,3,30,252,8,30,1,31,1,31,1,31,1,31,3,31,258,8,31,1,31,3,
        31,261,8,31,1,32,1,32,1,32,1,32,1,32,3,32,268,8,32,1,32,3,32,271,
        8,32,1,33,1,33,1,33,1,34,1,34,3,34,278,8,34,1,35,1,35,1,35,1,35,
        1,35,1,36,1,36,1,36,1,36,1,36,1,37,1,37,1,38,1,38,1,38,1,38,1,38,
        0,0,39,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
        42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,0,3,1,0,10,
        13,1,0,8,9,1,0,41,42,300,0,81,1,0,0,0,2,92,1,0,0,0,4,94,1,0,0,0,
        6,145,1,0,0,0,8,147,1,0,0,0,10,150,1,0,0,0,12,153,1,0,0,0,14,156,
        1,0,0,0,16,159,1,0,0,0,18,162,1,0,0,0,20,165,1,0,0,0,22,168,1,0,
        0,0,24,171,1,0,0,0,26,174,1,0,0,0,28,177,1,0,0,0,30,180,1,0,0,0,
        32,183,1,0,0,0,34,186,1,0,0,0,36,189,1,0,0,0,38,192,1,0,0,0,40,195,
        1,0,0,0,42,198,1,0,0,0,44,201,1,0,0,0,46,204,1,0,0,0,48,207,1,0,
        0,0,50,211,1,0,0,0,52,215,1,0,0,0,54,221,1,0,0,0,56,229,1,0,0,0,
        58,231,1,0,0,0,60,249,1,0,0,0,62,257,1,0,0,0,64,267,1,0,0,0,66,272,
        1,0,0,0,68,277,1,0,0,0,70,279,1,0,0,0,72,284,1,0,0,0,74,289,1,0,
        0,0,76,291,1,0,0,0,78,80,3,2,1,0,79,78,1,0,0,0,80,83,1,0,0,0,81,
        79,1,0,0,0,81,82,1,0,0,0,82,84,1,0,0,0,83,81,1,0,0,0,84,85,5,0,0,
        1,85,1,1,0,0,0,86,93,5,45,0,0,87,93,3,70,35,0,88,93,3,72,36,0,89,
        93,3,4,2,0,90,93,3,6,3,0,91,93,3,76,38,0,92,86,1,0,0,0,92,87,1,0,
        0,0,92,88,1,0,0,0,92,89,1,0,0,0,92,90,1,0,0,0,92,91,1,0,0,0,93,3,
        1,0,0,0,94,98,3,6,3,0,95,97,5,45,0,0,96,95,1,0,0,0,97,100,1,0,0,
        0,98,96,1,0,0,0,98,99,1,0,0,0,99,101,1,0,0,0,100,98,1,0,0,0,101,
        105,5,44,0,0,102,104,5,45,0,0,103,102,1,0,0,0,104,107,1,0,0,0,105,
        103,1,0,0,0,105,106,1,0,0,0,106,108,1,0,0,0,107,105,1,0,0,0,108,
        123,3,6,3,0,109,111,5,45,0,0,110,109,1,0,0,0,111,114,1,0,0,0,112,
        110,1,0,0,0,112,113,1,0,0,0,113,115,1,0,0,0,114,112,1,0,0,0,115,
        119,5,44,0,0,116,118,5,45,0,0,117,116,1,0,0,0,118,121,1,0,0,0,119,
        117,1,0,0,0,119,120,1,0,0,0,120,122,1,0,0,0,121,119,1,0,0,0,122,
        124,3,6,3,0,123,112,1,0,0,0,123,124,1,0,0,0,124,5,1,0,0,0,125,146,
        3,8,4,0,126,146,3,10,5,0,127,146,3,12,6,0,128,146,3,14,7,0,129,146,
        3,16,8,0,130,146,3,18,9,0,131,146,3,20,10,0,132,146,3,22,11,0,133,
        146,3,24,12,0,134,146,3,26,13,0,135,146,3,28,14,0,136,146,3,30,15,
        0,137,146,3,32,16,0,138,146,3,34,17,0,139,146,3,36,18,0,140,146,
        3,38,19,0,141,146,3,40,20,0,142,146,3,42,21,0,143,146,3,44,22,0,
        144,146,3,46,23,0,145,125,1,0,0,0,145,126,1,0,0,0,145,127,1,0,0,
        0,145,128,1,0,0,0,145,129,1,0,0,0,145,130,1,0,0,0,145,131,1,0,0,
        0,145,132,1,0,0,0,145,133,1,0,0,0,145,134,1,0,0,0,145,135,1,0,0,
        0,145,136,1,0,0,0,145,137,1,0,0,0,145,138,1,0,0,0,145,139,1,0,0,
        0,145,140,1,0,0,0,145,141,1,0,0,0,145,142,1,0,0,0,145,143,1,0,0,
        0,145,144,1,0,0,0,146,7,1,0,0,0,147,148,5,21,0,0,148,149,3,52,26,
        0,149,9,1,0,0,0,150,151,5,33,0,0,151,152,3,48,24,0,152,11,1,0,0,
        0,153,154,5,22,0,0,154,155,3,52,26,0,155,13,1,0,0,0,156,157,5,23,
        0,0,157,158,3,52,26,0,158,15,1,0,0,0,159,160,5,34,0,0,160,161,3,
        52,26,0,161,17,1,0,0,0,162,163,5,24,0,0,163,164,3,52,26,0,164,19,
        1,0,0,0,165,166,5,35,0,0,166,167,3,50,25,0,167,21,1,0,0,0,168,169,
        5,36,0,0,169,170,3,50,25,0,170,23,1,0,0,0,171,172,5,37,0,0,172,173,
        3,50,25,0,173,25,1,0,0,0,174,175,5,25,0,0,175,176,3,54,27,0,176,
        27,1,0,0,0,177,178,5,26,0,0,178,179,3,52,26,0,179,29,1,0,0,0,180,
        181,5,27,0,0,181,182,3,52,26,0,182,31,1,0,0,0,183,184,5,28,0,0,184,
        185,3,50,25,0,185,33,1,0,0,0,186,187,5,29,0,0,187,188,3,52,26,0,
        188,35,1,0,0,0,189,190,5,40,0,0,190,191,3,50,25,0,191,37,1,0,0,0,
        192,193,5,38,0,0,193,194,3,50,25,0,194,39,1,0,0,0,195,196,5,39,0,
        0,196,197,3,50,25,0,197,41,1,0,0,0,198,199,5,30,0,0,199,200,3,52,
        26,0,200,43,1,0,0,0,201,202,5,31,0,0,202,203,3,52,26,0,203,45,1,
        0,0,0,204,205,5,32,0,0,205,206,3,52,26,0,206,47,1,0,0,0,207,208,
        3,60,30,0,208,209,5,46,0,0,209,210,3,68,34,0,210,49,1,0,0,0,211,
        212,3,62,31,0,212,213,5,46,0,0,213,214,3,68,34,0,214,51,1,0,0,0,
        215,216,3,62,31,0,216,217,5,46,0,0,217,218,3,68,34,0,218,219,5,46,
        0,0,219,220,3,68,34,0,220,53,1,0,0,0,221,222,3,62,31,0,222,223,5,
        46,0,0,223,224,3,68,34,0,224,225,5,46,0,0,225,226,3,68,34,0,226,
        227,5,46,0,0,227,228,3,68,34,0,228,55,1,0,0,0,229,230,7,0,0,0,230,
        57,1,0,0,0,231,247,5,43,0,0,232,236,5,1,0,0,233,235,5,48,0,0,234,
        233,1,0,0,0,235,238,1,0,0,0,236,234,1,0,0,0,236,237,1,0,0,0,237,
        239,1,0,0,0,238,236,1,0,0,0,239,243,5,6,0,0,240,242,5,48,0,0,241,
        240,1,0,0,0,242,245,1,0,0,0,243,241,1,0,0,0,243,244,1,0,0,0,244,
        246,1,0,0,0,245,243,1,0,0,0,246,248,5,2,0,0,247,232,1,0,0,0,247,
        248,1,0,0,0,248,59,1,0,0,0,249,251,5,18,0,0,250,252,5,8,0,0,251,
        250,1,0,0,0,251,252,1,0,0,0,252,61,1,0,0,0,253,258,5,17,0,0,254,
        258,5,16,0,0,255,258,3,56,28,0,256,258,3,58,29,0,257,253,1,0,0,0,
        257,254,1,0,0,0,257,255,1,0,0,0,257,256,1,0,0,0,258,260,1,0,0,0,
        259,261,5,8,0,0,260,259,1,0,0,0,260,261,1,0,0,0,261,63,1,0,0,0,262,
        268,5,17,0,0,263,268,5,15,0,0,264,268,5,14,0,0,265,268,3,56,28,0,
        266,268,3,58,29,0,267,262,1,0,0,0,267,263,1,0,0,0,267,264,1,0,0,
        0,267,265,1,0,0,0,267,266,1,0,0,0,268,270,1,0,0,0,269,271,7,1,0,
        0,270,269,1,0,0,0,270,271,1,0,0,0,271,65,1,0,0,0,272,273,5,5,0,0,
        273,274,3,64,32,0,274,67,1,0,0,0,275,278,3,64,32,0,276,278,3,66,
        33,0,277,275,1,0,0,0,277,276,1,0,0,0,278,69,1,0,0,0,279,280,5,3,
        0,0,280,281,3,62,31,0,281,282,3,68,34,0,282,283,3,58,29,0,283,71,
        1,0,0,0,284,285,5,4,0,0,285,286,3,62,31,0,286,287,3,68,34,0,287,
        288,3,68,34,0,288,73,1,0,0,0,289,290,7,2,0,0,290,75,1,0,0,0,291,
        292,5,43,0,0,292,293,3,74,37,0,293,294,5,6,0,0,294,77,1,0,0,0,17,
        81,92,98,105,112,119,123,145,236,243,247,251,257,260,267,270,277
    ]

class VshParser ( Parser ):

    grammarFileName = "Vsh.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "<INVALID>", "<INVALID>", 
                     "'-'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'+'", "<INVALID>", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "MACRO_MATRIX_4X4_MULTIPLY", 
                      "MACRO_NORMALIZE_3", "NEGATE", "INTEGER", "FLOAT", 
                      "DESTINATION_MASK", "SWIZZLE_MASK", "REG_Cx_BARE", 
                      "REG_Cx_BRACKETED", "REG_Cx_RELATIVE_A_FIRST", "REG_Cx_RELATIVE_A_SECOND", 
                      "REG_R12", "REG_INPUT", "REG_OUTPUT", "REG_Rx", "REG_A0", 
                      "DEF", "OP_NOP", "OP_ADD", "OP_DP3", "OP_DP4", "OP_DST", 
                      "OP_MAD", "OP_MAX", "OP_MIN", "OP_MOV", "OP_MUL", 
                      "OP_SGE", "OP_SLT", "OP_SUB", "OP_ARL", "OP_DPH", 
                      "OP_EXPP", "OP_LIT", "OP_LOGP", "OP_RCP", "OP_RSQ", 
                      "OP_RCC", "TYPE_VECTOR", "TYPE_MATRIX4", "UNIFORM_IDENTIFIER", 
                      "COMBINE", "NEWLINE", "SEP", "SEP_MULTILINE", "WHITESPACE", 
                      "LINE_COMMENT", "BLOCK_COMMENT", "BAD_INPUT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_combined_operation = 2
    RULE_operation = 3
    RULE_op_add = 4
    RULE_op_arl = 5
    RULE_op_dp3 = 6
    RULE_op_dp4 = 7
    RULE_op_dph = 8
    RULE_op_dst = 9
    RULE_op_expp = 10
    RULE_op_lit = 11
    RULE_op_logp = 12
    RULE_op_mad = 13
    RULE_op_max = 14
    RULE_op_min = 15
    RULE_op_mov = 16
    RULE_op_mul = 17
    RULE_op_rcc = 18
    RULE_op_rcp = 19
    RULE_op_rsq = 20
    RULE_op_sge = 21
    RULE_op_slt = 22
    RULE_op_sub = 23
    RULE_p_a0_in = 24
    RULE_p_out_in = 25
    RULE_p_out_in_in = 26
    RULE_p_out_in_in_in = 27
    RULE_reg_const = 28
    RULE_uniform_const = 29
    RULE_p_a0_output = 30
    RULE_p_output = 31
    RULE_p_input_raw = 32
    RULE_p_input_negated = 33
    RULE_p_input = 34
    RULE_macro_matrix_4x4_multiply = 35
    RULE_macro_norm_3 = 36
    RULE_uniform_type = 37
    RULE_uniform_declaration = 38

    ruleNames =  [ "program", "statement", "combined_operation", "operation", 
                   "op_add", "op_arl", "op_dp3", "op_dp4", "op_dph", "op_dst", 
                   "op_expp", "op_lit", "op_logp", "op_mad", "op_max", "op_min", 
                   "op_mov", "op_mul", "op_rcc", "op_rcp", "op_rsq", "op_sge", 
                   "op_slt", "op_sub", "p_a0_in", "p_out_in", "p_out_in_in", 
                   "p_out_in_in_in", "reg_const", "uniform_const", "p_a0_output", 
                   "p_output", "p_input_raw", "p_input_negated", "p_input", 
                   "macro_matrix_4x4_multiply", "macro_norm_3", "uniform_type", 
                   "uniform_declaration" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    MACRO_MATRIX_4X4_MULTIPLY=3
    MACRO_NORMALIZE_3=4
    NEGATE=5
    INTEGER=6
    FLOAT=7
    DESTINATION_MASK=8
    SWIZZLE_MASK=9
    REG_Cx_BARE=10
    REG_Cx_BRACKETED=11
    REG_Cx_RELATIVE_A_FIRST=12
    REG_Cx_RELATIVE_A_SECOND=13
    REG_R12=14
    REG_INPUT=15
    REG_OUTPUT=16
    REG_Rx=17
    REG_A0=18
    DEF=19
    OP_NOP=20
    OP_ADD=21
    OP_DP3=22
    OP_DP4=23
    OP_DST=24
    OP_MAD=25
    OP_MAX=26
    OP_MIN=27
    OP_MOV=28
    OP_MUL=29
    OP_SGE=30
    OP_SLT=31
    OP_SUB=32
    OP_ARL=33
    OP_DPH=34
    OP_EXPP=35
    OP_LIT=36
    OP_LOGP=37
    OP_RCP=38
    OP_RSQ=39
    OP_RCC=40
    TYPE_VECTOR=41
    TYPE_MATRIX4=42
    UNIFORM_IDENTIFIER=43
    COMBINE=44
    NEWLINE=45
    SEP=46
    SEP_MULTILINE=47
    WHITESPACE=48
    LINE_COMMENT=49
    BLOCK_COMMENT=50
    BAD_INPUT=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(VshParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VshParser.StatementContext)
            else:
                return self.getTypedRuleContext(VshParser.StatementContext,i)


        def getRuleIndex(self):
            return VshParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = VshParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 46179486269464) != 0):
                self.state = 78
                self.statement()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self.match(VshParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(VshParser.NEWLINE, 0)

        def macro_matrix_4x4_multiply(self):
            return self.getTypedRuleContext(VshParser.Macro_matrix_4x4_multiplyContext,0)


        def macro_norm_3(self):
            return self.getTypedRuleContext(VshParser.Macro_norm_3Context,0)


        def combined_operation(self):
            return self.getTypedRuleContext(VshParser.Combined_operationContext,0)


        def operation(self):
            return self.getTypedRuleContext(VshParser.OperationContext,0)


        def uniform_declaration(self):
            return self.getTypedRuleContext(VshParser.Uniform_declarationContext,0)


        def getRuleIndex(self):
            return VshParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = VshParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.match(VshParser.NEWLINE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.macro_matrix_4x4_multiply()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 88
                self.macro_norm_3()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 89
                self.combined_operation()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 90
                self.operation()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 91
                self.uniform_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Combined_operationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VshParser.OperationContext)
            else:
                return self.getTypedRuleContext(VshParser.OperationContext,i)


        def COMBINE(self, i:int=None):
            if i is None:
                return self.getTokens(VshParser.COMBINE)
            else:
                return self.getToken(VshParser.COMBINE, i)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(VshParser.NEWLINE)
            else:
                return self.getToken(VshParser.NEWLINE, i)

        def getRuleIndex(self):
            return VshParser.RULE_combined_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCombined_operation" ):
                listener.enterCombined_operation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCombined_operation" ):
                listener.exitCombined_operation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCombined_operation" ):
                return visitor.visitCombined_operation(self)
            else:
                return visitor.visitChildren(self)




    def combined_operation(self):

        localctx = VshParser.Combined_operationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_combined_operation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.operation()
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 95
                self.match(VshParser.NEWLINE)
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 101
            self.match(VshParser.COMBINE)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==45:
                self.state = 102
                self.match(VshParser.NEWLINE)
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 108
            self.operation()
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 112
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==45:
                    self.state = 109
                    self.match(VshParser.NEWLINE)
                    self.state = 114
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 115
                self.match(VshParser.COMBINE)
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==45:
                    self.state = 116
                    self.match(VshParser.NEWLINE)
                    self.state = 121
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 122
                self.operation()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op_add(self):
            return self.getTypedRuleContext(VshParser.Op_addContext,0)


        def op_arl(self):
            return self.getTypedRuleContext(VshParser.Op_arlContext,0)


        def op_dp3(self):
            return self.getTypedRuleContext(VshParser.Op_dp3Context,0)


        def op_dp4(self):
            return self.getTypedRuleContext(VshParser.Op_dp4Context,0)


        def op_dph(self):
            return self.getTypedRuleContext(VshParser.Op_dphContext,0)


        def op_dst(self):
            return self.getTypedRuleContext(VshParser.Op_dstContext,0)


        def op_expp(self):
            return self.getTypedRuleContext(VshParser.Op_exppContext,0)


        def op_lit(self):
            return self.getTypedRuleContext(VshParser.Op_litContext,0)


        def op_logp(self):
            return self.getTypedRuleContext(VshParser.Op_logpContext,0)


        def op_mad(self):
            return self.getTypedRuleContext(VshParser.Op_madContext,0)


        def op_max(self):
            return self.getTypedRuleContext(VshParser.Op_maxContext,0)


        def op_min(self):
            return self.getTypedRuleContext(VshParser.Op_minContext,0)


        def op_mov(self):
            return self.getTypedRuleContext(VshParser.Op_movContext,0)


        def op_mul(self):
            return self.getTypedRuleContext(VshParser.Op_mulContext,0)


        def op_rcc(self):
            return self.getTypedRuleContext(VshParser.Op_rccContext,0)


        def op_rcp(self):
            return self.getTypedRuleContext(VshParser.Op_rcpContext,0)


        def op_rsq(self):
            return self.getTypedRuleContext(VshParser.Op_rsqContext,0)


        def op_sge(self):
            return self.getTypedRuleContext(VshParser.Op_sgeContext,0)


        def op_slt(self):
            return self.getTypedRuleContext(VshParser.Op_sltContext,0)


        def op_sub(self):
            return self.getTypedRuleContext(VshParser.Op_subContext,0)


        def getRuleIndex(self):
            return VshParser.RULE_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperation" ):
                listener.enterOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperation" ):
                listener.exitOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperation" ):
                return visitor.visitOperation(self)
            else:
                return visitor.visitChildren(self)




    def operation(self):

        localctx = VshParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_operation)
        try:
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.op_add()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
                self.op_arl()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 127
                self.op_dp3()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 4)
                self.state = 128
                self.op_dp4()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 5)
                self.state = 129
                self.op_dph()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 6)
                self.state = 130
                self.op_dst()
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 7)
                self.state = 131
                self.op_expp()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 8)
                self.state = 132
                self.op_lit()
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 9)
                self.state = 133
                self.op_logp()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 10)
                self.state = 134
                self.op_mad()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 11)
                self.state = 135
                self.op_max()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 12)
                self.state = 136
                self.op_min()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 13)
                self.state = 137
                self.op_mov()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 14)
                self.state = 138
                self.op_mul()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 15)
                self.state = 139
                self.op_rcc()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 16)
                self.state = 140
                self.op_rcp()
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 17)
                self.state = 141
                self.op_rsq()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 18)
                self.state = 142
                self.op_sge()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 19)
                self.state = 143
                self.op_slt()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 20)
                self.state = 144
                self.op_sub()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_addContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_ADD(self):
            return self.getToken(VshParser.OP_ADD, 0)

        def p_out_in_in(self):
            return self.getTypedRuleContext(VshParser.P_out_in_inContext,0)


        def getRuleIndex(self):
            return VshParser.RULE_op_add

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_add" ):
                listener.enterOp_add(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_add" ):
                listener.exitOp_add(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_add" ):
                return visitor.visitOp_add(self)
            else:
                return visitor.visitChildren(self)




    def op_add(self):

        localctx = VshParser.Op_addContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_op_add)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(VshParser.OP_ADD)
            self.state = 148
            self.p_out_in_in()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_arlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_ARL(self):
            return self.getToken(VshParser.OP_ARL, 0)

        def p_a0_in(self):
            return self.getTypedRuleContext(VshParser.P_a0_inContext,0)


        def getRuleIndex(self):
            return VshParser.RULE_op_arl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_arl" ):
                listener.enterOp_arl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_arl" ):
                listener.exitOp_arl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_arl" ):
                return visitor.visitOp_arl(self)
            else:
                return visitor.visitChildren(self)




    def op_arl(self):

        localctx = VshParser.Op_arlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_op_arl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(VshParser.OP_ARL)
            self.state = 151
            self.p_a0_in()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_dp3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_DP3(self):
            return self.getToken(VshParser.OP_DP3, 0)

        def p_out_in_in(self):
            return self.getTypedRuleContext(VshParser.P_out_in_inContext,0)


        def getRuleIndex(self):
            return VshParser.RULE_op_dp3

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_dp3" ):
                listener.enterOp_dp3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_dp3" ):
                listener.exitOp_dp3(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_dp3" ):
                return visitor.visitOp_dp3(self)
            else:
                return visitor.visitChildren(self)




    def op_dp3(self):

        localctx = VshParser.Op_dp3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_op_dp3)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(VshParser.OP_DP3)
            self.state = 154
            self.p_out_in_in()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_dp4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_DP4(self):
            return self.getToken(VshParser.OP_DP4, 0)

        def p_out_in_in(self):
            return self.getTypedRuleContext(VshParser.P_out_in_inContext,0)


        def getRuleIndex(self):
            return VshParser.RULE_op_dp4

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_dp4" ):
                listener.enterOp_dp4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_dp4" ):
                listener.exitOp_dp4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_dp4" ):
                return visitor.visitOp_dp4(self)
            else:
                return visitor.visitChildren(self)




    def op_dp4(self):

        localctx = VshParser.Op_dp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_op_dp4)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(VshParser.OP_DP4)
            self.state = 157
            self.p_out_in_in()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_dphContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_DPH(self):
            return self.getToken(VshParser.OP_DPH, 0)

        def p_out_in_in(self):
            return self.getTypedRuleContext(VshParser.P_out_in_inContext,0)


        def getRuleIndex(self):
            return VshParser.RULE_op_dph

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_dph" ):
                listener.enterOp_dph(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_dph" ):
                listener.exitOp_dph(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_dph" ):
                return visitor.visitOp_dph(self)
            else:
                return visitor.visitChildren(self)




    def op_dph(self):

        localctx = VshParser.Op_dphContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_op_dph)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(VshParser.OP_DPH)
            self.state = 160
            self.p_out_in_in()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_dstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_DST(self):
            return self.getToken(VshParser.OP_DST, 0)

        def p_out_in_in(self):
            return self.getTypedRuleContext(VshParser.P_out_in_inContext,0)


        def getRuleIndex(self):
            return VshParser.RULE_op_dst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_dst" ):
                listener.enterOp_dst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_dst" ):
                listener.exitOp_dst(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_dst" ):
                return visitor.visitOp_dst(self)
            else:
                return visitor.visitChildren(self)




    def op_dst(self):

        localctx = VshParser.Op_dstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_op_dst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(VshParser.OP_DST)
            self.state = 163
            self.p_out_in_in()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_exppContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_EXPP(self):
            return self.getToken(VshParser.OP_EXPP, 0)

        def p_out_in(self):
            return self.getTypedRuleContext(VshParser.P_out_inContext,0)


        def getRuleIndex(self):
            return VshParser.RULE_op_expp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_expp" ):
                listener.enterOp_expp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_expp" ):
                listener.exitOp_expp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_expp" ):
                return visitor.visitOp_expp(self)
            else:
                return visitor.visitChildren(self)




    def op_expp(self):

        localctx = VshParser.Op_exppContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_op_expp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(VshParser.OP_EXPP)
            self.state = 166
            self.p_out_in()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_LIT(self):
            return self.getToken(VshParser.OP_LIT, 0)

        def p_out_in(self):
            return self.getTypedRuleContext(VshParser.P_out_inContext,0)


        def getRuleIndex(self):
            return VshParser.RULE_op_lit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_lit" ):
                listener.enterOp_lit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_lit" ):
                listener.exitOp_lit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_lit" ):
                return visitor.visitOp_lit(self)
            else:
                return visitor.visitChildren(self)




    def op_lit(self):

        localctx = VshParser.Op_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_op_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(VshParser.OP_LIT)
            self.state = 169
            self.p_out_in()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_logpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_LOGP(self):
            return self.getToken(VshParser.OP_LOGP, 0)

        def p_out_in(self):
            return self.getTypedRuleContext(VshParser.P_out_inContext,0)


        def getRuleIndex(self):
            return VshParser.RULE_op_logp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_logp" ):
                listener.enterOp_logp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_logp" ):
                listener.exitOp_logp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_logp" ):
                return visitor.visitOp_logp(self)
            else:
                return visitor.visitChildren(self)




    def op_logp(self):

        localctx = VshParser.Op_logpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_op_logp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(VshParser.OP_LOGP)
            self.state = 172
            self.p_out_in()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_madContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_MAD(self):
            return self.getToken(VshParser.OP_MAD, 0)

        def p_out_in_in_in(self):
            return self.getTypedRuleContext(VshParser.P_out_in_in_inContext,0)


        def getRuleIndex(self):
            return VshParser.RULE_op_mad

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_mad" ):
                listener.enterOp_mad(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_mad" ):
                listener.exitOp_mad(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_mad" ):
                return visitor.visitOp_mad(self)
            else:
                return visitor.visitChildren(self)




    def op_mad(self):

        localctx = VshParser.Op_madContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_op_mad)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(VshParser.OP_MAD)
            self.state = 175
            self.p_out_in_in_in()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_maxContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_MAX(self):
            return self.getToken(VshParser.OP_MAX, 0)

        def p_out_in_in(self):
            return self.getTypedRuleContext(VshParser.P_out_in_inContext,0)


        def getRuleIndex(self):
            return VshParser.RULE_op_max

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_max" ):
                listener.enterOp_max(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_max" ):
                listener.exitOp_max(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_max" ):
                return visitor.visitOp_max(self)
            else:
                return visitor.visitChildren(self)




    def op_max(self):

        localctx = VshParser.Op_maxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_op_max)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(VshParser.OP_MAX)
            self.state = 178
            self.p_out_in_in()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_minContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_MIN(self):
            return self.getToken(VshParser.OP_MIN, 0)

        def p_out_in_in(self):
            return self.getTypedRuleContext(VshParser.P_out_in_inContext,0)


        def getRuleIndex(self):
            return VshParser.RULE_op_min

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_min" ):
                listener.enterOp_min(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_min" ):
                listener.exitOp_min(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_min" ):
                return visitor.visitOp_min(self)
            else:
                return visitor.visitChildren(self)




    def op_min(self):

        localctx = VshParser.Op_minContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_op_min)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(VshParser.OP_MIN)
            self.state = 181
            self.p_out_in_in()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_movContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_MOV(self):
            return self.getToken(VshParser.OP_MOV, 0)

        def p_out_in(self):
            return self.getTypedRuleContext(VshParser.P_out_inContext,0)


        def getRuleIndex(self):
            return VshParser.RULE_op_mov

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_mov" ):
                listener.enterOp_mov(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_mov" ):
                listener.exitOp_mov(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_mov" ):
                return visitor.visitOp_mov(self)
            else:
                return visitor.visitChildren(self)




    def op_mov(self):

        localctx = VshParser.Op_movContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_op_mov)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(VshParser.OP_MOV)
            self.state = 184
            self.p_out_in()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_mulContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_MUL(self):
            return self.getToken(VshParser.OP_MUL, 0)

        def p_out_in_in(self):
            return self.getTypedRuleContext(VshParser.P_out_in_inContext,0)


        def getRuleIndex(self):
            return VshParser.RULE_op_mul

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_mul" ):
                listener.enterOp_mul(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_mul" ):
                listener.exitOp_mul(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_mul" ):
                return visitor.visitOp_mul(self)
            else:
                return visitor.visitChildren(self)




    def op_mul(self):

        localctx = VshParser.Op_mulContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_op_mul)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(VshParser.OP_MUL)
            self.state = 187
            self.p_out_in_in()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_rccContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_RCC(self):
            return self.getToken(VshParser.OP_RCC, 0)

        def p_out_in(self):
            return self.getTypedRuleContext(VshParser.P_out_inContext,0)


        def getRuleIndex(self):
            return VshParser.RULE_op_rcc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_rcc" ):
                listener.enterOp_rcc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_rcc" ):
                listener.exitOp_rcc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_rcc" ):
                return visitor.visitOp_rcc(self)
            else:
                return visitor.visitChildren(self)




    def op_rcc(self):

        localctx = VshParser.Op_rccContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_op_rcc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(VshParser.OP_RCC)
            self.state = 190
            self.p_out_in()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_rcpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_RCP(self):
            return self.getToken(VshParser.OP_RCP, 0)

        def p_out_in(self):
            return self.getTypedRuleContext(VshParser.P_out_inContext,0)


        def getRuleIndex(self):
            return VshParser.RULE_op_rcp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_rcp" ):
                listener.enterOp_rcp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_rcp" ):
                listener.exitOp_rcp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_rcp" ):
                return visitor.visitOp_rcp(self)
            else:
                return visitor.visitChildren(self)




    def op_rcp(self):

        localctx = VshParser.Op_rcpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_op_rcp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(VshParser.OP_RCP)
            self.state = 193
            self.p_out_in()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_rsqContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_RSQ(self):
            return self.getToken(VshParser.OP_RSQ, 0)

        def p_out_in(self):
            return self.getTypedRuleContext(VshParser.P_out_inContext,0)


        def getRuleIndex(self):
            return VshParser.RULE_op_rsq

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_rsq" ):
                listener.enterOp_rsq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_rsq" ):
                listener.exitOp_rsq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_rsq" ):
                return visitor.visitOp_rsq(self)
            else:
                return visitor.visitChildren(self)




    def op_rsq(self):

        localctx = VshParser.Op_rsqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_op_rsq)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(VshParser.OP_RSQ)
            self.state = 196
            self.p_out_in()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_sgeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_SGE(self):
            return self.getToken(VshParser.OP_SGE, 0)

        def p_out_in_in(self):
            return self.getTypedRuleContext(VshParser.P_out_in_inContext,0)


        def getRuleIndex(self):
            return VshParser.RULE_op_sge

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_sge" ):
                listener.enterOp_sge(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_sge" ):
                listener.exitOp_sge(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_sge" ):
                return visitor.visitOp_sge(self)
            else:
                return visitor.visitChildren(self)




    def op_sge(self):

        localctx = VshParser.Op_sgeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_op_sge)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(VshParser.OP_SGE)
            self.state = 199
            self.p_out_in_in()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_sltContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_SLT(self):
            return self.getToken(VshParser.OP_SLT, 0)

        def p_out_in_in(self):
            return self.getTypedRuleContext(VshParser.P_out_in_inContext,0)


        def getRuleIndex(self):
            return VshParser.RULE_op_slt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_slt" ):
                listener.enterOp_slt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_slt" ):
                listener.exitOp_slt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_slt" ):
                return visitor.visitOp_slt(self)
            else:
                return visitor.visitChildren(self)




    def op_slt(self):

        localctx = VshParser.Op_sltContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_op_slt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(VshParser.OP_SLT)
            self.state = 202
            self.p_out_in_in()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_subContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_SUB(self):
            return self.getToken(VshParser.OP_SUB, 0)

        def p_out_in_in(self):
            return self.getTypedRuleContext(VshParser.P_out_in_inContext,0)


        def getRuleIndex(self):
            return VshParser.RULE_op_sub

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_sub" ):
                listener.enterOp_sub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_sub" ):
                listener.exitOp_sub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_sub" ):
                return visitor.visitOp_sub(self)
            else:
                return visitor.visitChildren(self)




    def op_sub(self):

        localctx = VshParser.Op_subContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_op_sub)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(VshParser.OP_SUB)
            self.state = 205
            self.p_out_in_in()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class P_a0_inContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def p_a0_output(self):
            return self.getTypedRuleContext(VshParser.P_a0_outputContext,0)


        def SEP(self):
            return self.getToken(VshParser.SEP, 0)

        def p_input(self):
            return self.getTypedRuleContext(VshParser.P_inputContext,0)


        def getRuleIndex(self):
            return VshParser.RULE_p_a0_in

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterP_a0_in" ):
                listener.enterP_a0_in(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitP_a0_in" ):
                listener.exitP_a0_in(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitP_a0_in" ):
                return visitor.visitP_a0_in(self)
            else:
                return visitor.visitChildren(self)




    def p_a0_in(self):

        localctx = VshParser.P_a0_inContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_p_a0_in)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.p_a0_output()
            self.state = 208
            self.match(VshParser.SEP)
            self.state = 209
            self.p_input()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class P_out_inContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def p_output(self):
            return self.getTypedRuleContext(VshParser.P_outputContext,0)


        def SEP(self):
            return self.getToken(VshParser.SEP, 0)

        def p_input(self):
            return self.getTypedRuleContext(VshParser.P_inputContext,0)


        def getRuleIndex(self):
            return VshParser.RULE_p_out_in

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterP_out_in" ):
                listener.enterP_out_in(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitP_out_in" ):
                listener.exitP_out_in(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitP_out_in" ):
                return visitor.visitP_out_in(self)
            else:
                return visitor.visitChildren(self)




    def p_out_in(self):

        localctx = VshParser.P_out_inContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_p_out_in)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.p_output()
            self.state = 212
            self.match(VshParser.SEP)
            self.state = 213
            self.p_input()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class P_out_in_inContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def p_output(self):
            return self.getTypedRuleContext(VshParser.P_outputContext,0)


        def SEP(self, i:int=None):
            if i is None:
                return self.getTokens(VshParser.SEP)
            else:
                return self.getToken(VshParser.SEP, i)

        def p_input(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VshParser.P_inputContext)
            else:
                return self.getTypedRuleContext(VshParser.P_inputContext,i)


        def getRuleIndex(self):
            return VshParser.RULE_p_out_in_in

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterP_out_in_in" ):
                listener.enterP_out_in_in(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitP_out_in_in" ):
                listener.exitP_out_in_in(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitP_out_in_in" ):
                return visitor.visitP_out_in_in(self)
            else:
                return visitor.visitChildren(self)




    def p_out_in_in(self):

        localctx = VshParser.P_out_in_inContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_p_out_in_in)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.p_output()
            self.state = 216
            self.match(VshParser.SEP)
            self.state = 217
            self.p_input()
            self.state = 218
            self.match(VshParser.SEP)
            self.state = 219
            self.p_input()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class P_out_in_in_inContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def p_output(self):
            return self.getTypedRuleContext(VshParser.P_outputContext,0)


        def SEP(self, i:int=None):
            if i is None:
                return self.getTokens(VshParser.SEP)
            else:
                return self.getToken(VshParser.SEP, i)

        def p_input(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VshParser.P_inputContext)
            else:
                return self.getTypedRuleContext(VshParser.P_inputContext,i)


        def getRuleIndex(self):
            return VshParser.RULE_p_out_in_in_in

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterP_out_in_in_in" ):
                listener.enterP_out_in_in_in(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitP_out_in_in_in" ):
                listener.exitP_out_in_in_in(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitP_out_in_in_in" ):
                return visitor.visitP_out_in_in_in(self)
            else:
                return visitor.visitChildren(self)




    def p_out_in_in_in(self):

        localctx = VshParser.P_out_in_in_inContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_p_out_in_in_in)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.p_output()
            self.state = 222
            self.match(VshParser.SEP)
            self.state = 223
            self.p_input()
            self.state = 224
            self.match(VshParser.SEP)
            self.state = 225
            self.p_input()
            self.state = 226
            self.match(VshParser.SEP)
            self.state = 227
            self.p_input()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Reg_constContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REG_Cx_BARE(self):
            return self.getToken(VshParser.REG_Cx_BARE, 0)

        def REG_Cx_BRACKETED(self):
            return self.getToken(VshParser.REG_Cx_BRACKETED, 0)

        def REG_Cx_RELATIVE_A_FIRST(self):
            return self.getToken(VshParser.REG_Cx_RELATIVE_A_FIRST, 0)

        def REG_Cx_RELATIVE_A_SECOND(self):
            return self.getToken(VshParser.REG_Cx_RELATIVE_A_SECOND, 0)

        def getRuleIndex(self):
            return VshParser.RULE_reg_const

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReg_const" ):
                listener.enterReg_const(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReg_const" ):
                listener.exitReg_const(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReg_const" ):
                return visitor.visitReg_const(self)
            else:
                return visitor.visitChildren(self)




    def reg_const(self):

        localctx = VshParser.Reg_constContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_reg_const)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15360) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Uniform_constContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNIFORM_IDENTIFIER(self):
            return self.getToken(VshParser.UNIFORM_IDENTIFIER, 0)

        def INTEGER(self):
            return self.getToken(VshParser.INTEGER, 0)

        def WHITESPACE(self, i:int=None):
            if i is None:
                return self.getTokens(VshParser.WHITESPACE)
            else:
                return self.getToken(VshParser.WHITESPACE, i)

        def getRuleIndex(self):
            return VshParser.RULE_uniform_const

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUniform_const" ):
                listener.enterUniform_const(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUniform_const" ):
                listener.exitUniform_const(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUniform_const" ):
                return visitor.visitUniform_const(self)
            else:
                return visitor.visitChildren(self)




    def uniform_const(self):

        localctx = VshParser.Uniform_constContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_uniform_const)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(VshParser.UNIFORM_IDENTIFIER)
            self.state = 247
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 232
                self.match(VshParser.T__0)
                self.state = 236
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==48:
                    self.state = 233
                    self.match(VshParser.WHITESPACE)
                    self.state = 238
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 239
                self.match(VshParser.INTEGER)
                self.state = 243
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==48:
                    self.state = 240
                    self.match(VshParser.WHITESPACE)
                    self.state = 245
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 246
                self.match(VshParser.T__1)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class P_a0_outputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REG_A0(self):
            return self.getToken(VshParser.REG_A0, 0)

        def DESTINATION_MASK(self):
            return self.getToken(VshParser.DESTINATION_MASK, 0)

        def getRuleIndex(self):
            return VshParser.RULE_p_a0_output

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterP_a0_output" ):
                listener.enterP_a0_output(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitP_a0_output" ):
                listener.exitP_a0_output(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitP_a0_output" ):
                return visitor.visitP_a0_output(self)
            else:
                return visitor.visitChildren(self)




    def p_a0_output(self):

        localctx = VshParser.P_a0_outputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_p_a0_output)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(VshParser.REG_A0)
            self.state = 251
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 250
                self.match(VshParser.DESTINATION_MASK)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class P_outputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REG_Rx(self):
            return self.getToken(VshParser.REG_Rx, 0)

        def REG_OUTPUT(self):
            return self.getToken(VshParser.REG_OUTPUT, 0)

        def reg_const(self):
            return self.getTypedRuleContext(VshParser.Reg_constContext,0)


        def uniform_const(self):
            return self.getTypedRuleContext(VshParser.Uniform_constContext,0)


        def DESTINATION_MASK(self):
            return self.getToken(VshParser.DESTINATION_MASK, 0)

        def getRuleIndex(self):
            return VshParser.RULE_p_output

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterP_output" ):
                listener.enterP_output(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitP_output" ):
                listener.exitP_output(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitP_output" ):
                return visitor.visitP_output(self)
            else:
                return visitor.visitChildren(self)




    def p_output(self):

        localctx = VshParser.P_outputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_p_output)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.state = 253
                self.match(VshParser.REG_Rx)
                pass
            elif token in [16]:
                self.state = 254
                self.match(VshParser.REG_OUTPUT)
                pass
            elif token in [10, 11, 12, 13]:
                self.state = 255
                self.reg_const()
                pass
            elif token in [43]:
                self.state = 256
                self.uniform_const()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 259
                self.match(VshParser.DESTINATION_MASK)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class P_input_rawContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REG_Rx(self):
            return self.getToken(VshParser.REG_Rx, 0)

        def REG_INPUT(self):
            return self.getToken(VshParser.REG_INPUT, 0)

        def REG_R12(self):
            return self.getToken(VshParser.REG_R12, 0)

        def reg_const(self):
            return self.getTypedRuleContext(VshParser.Reg_constContext,0)


        def uniform_const(self):
            return self.getTypedRuleContext(VshParser.Uniform_constContext,0)


        def SWIZZLE_MASK(self):
            return self.getToken(VshParser.SWIZZLE_MASK, 0)

        def DESTINATION_MASK(self):
            return self.getToken(VshParser.DESTINATION_MASK, 0)

        def getRuleIndex(self):
            return VshParser.RULE_p_input_raw

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterP_input_raw" ):
                listener.enterP_input_raw(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitP_input_raw" ):
                listener.exitP_input_raw(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitP_input_raw" ):
                return visitor.visitP_input_raw(self)
            else:
                return visitor.visitChildren(self)




    def p_input_raw(self):

        localctx = VshParser.P_input_rawContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_p_input_raw)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.state = 262
                self.match(VshParser.REG_Rx)
                pass
            elif token in [15]:
                self.state = 263
                self.match(VshParser.REG_INPUT)
                pass
            elif token in [14]:
                self.state = 264
                self.match(VshParser.REG_R12)
                pass
            elif token in [10, 11, 12, 13]:
                self.state = 265
                self.reg_const()
                pass
            elif token in [43]:
                self.state = 266
                self.uniform_const()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8 or _la==9:
                self.state = 269
                _la = self._input.LA(1)
                if not(_la==8 or _la==9):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class P_input_negatedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEGATE(self):
            return self.getToken(VshParser.NEGATE, 0)

        def p_input_raw(self):
            return self.getTypedRuleContext(VshParser.P_input_rawContext,0)


        def getRuleIndex(self):
            return VshParser.RULE_p_input_negated

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterP_input_negated" ):
                listener.enterP_input_negated(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitP_input_negated" ):
                listener.exitP_input_negated(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitP_input_negated" ):
                return visitor.visitP_input_negated(self)
            else:
                return visitor.visitChildren(self)




    def p_input_negated(self):

        localctx = VshParser.P_input_negatedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_p_input_negated)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(VshParser.NEGATE)
            self.state = 273
            self.p_input_raw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class P_inputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def p_input_raw(self):
            return self.getTypedRuleContext(VshParser.P_input_rawContext,0)


        def p_input_negated(self):
            return self.getTypedRuleContext(VshParser.P_input_negatedContext,0)


        def getRuleIndex(self):
            return VshParser.RULE_p_input

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterP_input" ):
                listener.enterP_input(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitP_input" ):
                listener.exitP_input(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitP_input" ):
                return visitor.visitP_input(self)
            else:
                return visitor.visitChildren(self)




    def p_input(self):

        localctx = VshParser.P_inputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_p_input)
        try:
            self.state = 277
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 11, 12, 13, 14, 15, 17, 43]:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.p_input_raw()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.p_input_negated()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Macro_matrix_4x4_multiplyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MACRO_MATRIX_4X4_MULTIPLY(self):
            return self.getToken(VshParser.MACRO_MATRIX_4X4_MULTIPLY, 0)

        def p_output(self):
            return self.getTypedRuleContext(VshParser.P_outputContext,0)


        def p_input(self):
            return self.getTypedRuleContext(VshParser.P_inputContext,0)


        def uniform_const(self):
            return self.getTypedRuleContext(VshParser.Uniform_constContext,0)


        def getRuleIndex(self):
            return VshParser.RULE_macro_matrix_4x4_multiply

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMacro_matrix_4x4_multiply" ):
                listener.enterMacro_matrix_4x4_multiply(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMacro_matrix_4x4_multiply" ):
                listener.exitMacro_matrix_4x4_multiply(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacro_matrix_4x4_multiply" ):
                return visitor.visitMacro_matrix_4x4_multiply(self)
            else:
                return visitor.visitChildren(self)




    def macro_matrix_4x4_multiply(self):

        localctx = VshParser.Macro_matrix_4x4_multiplyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_macro_matrix_4x4_multiply)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(VshParser.MACRO_MATRIX_4X4_MULTIPLY)
            self.state = 280
            self.p_output()
            self.state = 281
            self.p_input()
            self.state = 282
            self.uniform_const()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Macro_norm_3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MACRO_NORMALIZE_3(self):
            return self.getToken(VshParser.MACRO_NORMALIZE_3, 0)

        def p_output(self):
            return self.getTypedRuleContext(VshParser.P_outputContext,0)


        def p_input(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VshParser.P_inputContext)
            else:
                return self.getTypedRuleContext(VshParser.P_inputContext,i)


        def getRuleIndex(self):
            return VshParser.RULE_macro_norm_3

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMacro_norm_3" ):
                listener.enterMacro_norm_3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMacro_norm_3" ):
                listener.exitMacro_norm_3(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMacro_norm_3" ):
                return visitor.visitMacro_norm_3(self)
            else:
                return visitor.visitChildren(self)




    def macro_norm_3(self):

        localctx = VshParser.Macro_norm_3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_macro_norm_3)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(VshParser.MACRO_NORMALIZE_3)
            self.state = 285
            self.p_output()
            self.state = 286
            self.p_input()
            self.state = 287
            self.p_input()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Uniform_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE_MATRIX4(self):
            return self.getToken(VshParser.TYPE_MATRIX4, 0)

        def TYPE_VECTOR(self):
            return self.getToken(VshParser.TYPE_VECTOR, 0)

        def getRuleIndex(self):
            return VshParser.RULE_uniform_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUniform_type" ):
                listener.enterUniform_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUniform_type" ):
                listener.exitUniform_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUniform_type" ):
                return visitor.visitUniform_type(self)
            else:
                return visitor.visitChildren(self)




    def uniform_type(self):

        localctx = VshParser.Uniform_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_uniform_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            _la = self._input.LA(1)
            if not(_la==41 or _la==42):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Uniform_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNIFORM_IDENTIFIER(self):
            return self.getToken(VshParser.UNIFORM_IDENTIFIER, 0)

        def uniform_type(self):
            return self.getTypedRuleContext(VshParser.Uniform_typeContext,0)


        def INTEGER(self):
            return self.getToken(VshParser.INTEGER, 0)

        def getRuleIndex(self):
            return VshParser.RULE_uniform_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUniform_declaration" ):
                listener.enterUniform_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUniform_declaration" ):
                listener.exitUniform_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUniform_declaration" ):
                return visitor.visitUniform_declaration(self)
            else:
                return visitor.visitChildren(self)




    def uniform_declaration(self):

        localctx = VshParser.Uniform_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_uniform_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.match(VshParser.UNIFORM_IDENTIFIER)
            self.state = 292
            self.uniform_type()
            self.state = 293
            self.match(VshParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





