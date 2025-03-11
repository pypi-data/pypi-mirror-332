from ply import yacc
from ply.yacc import LRParser
from ply.yacc import YaccError
from relic.core.errors import RelicToolError

from relic.sga.v2.arciv import lexer

tokens = lexer.tokens


def p_root(p):
    """
    expression  : dict_kvs
    """
    p[0] = p[1]


def p_list(p):
    """
    list    : empty
            | '{' list_items '}'
    """
    if len(p) == 2:
        p[0] = {}
    else:
        p[0] = p[2]


def p_list_items(p):
    """
    list_items  : list_item
                | list_items ','
                | list_items ',' list_item
    """
    if len(p) == 2:
        p[0] = [p[1]]  # make item into a list
    elif len(p) == 3:
        p[0] = p[1]  # copy list; we are just consuming an optional comma
    elif len(p) == 4:
        p[0] = p[1]
        p[0] += [p[3]]
    else:
        raise NotImplementedError(len(p))


def p_list_item(p):
    """
    list_item   : dict
    """

    p[0] = p[1]


def p_dict(p):
    """
    dict    : empty
            | '{' dict_kvs '}'
    """

    if len(p) == 2:
        p[0] = {}
    else:
        p[0] = p[2]


def p_error(p):
    raise RelicToolError(f"Parsing Error: `{p}`") from YaccError(p)


def p_dict_kvs(p):
    """
    dict_kvs    : kv
                | dict_kvs ','
                | dict_kvs ',' kv
    """
    if len(p) == 2:
        k, v = p[1]
        p[0] = {k: v}  # make item into a dict
    elif len(p) == 3:
        p[0] = p[1]  # copy dict; we are just consuming an optional comma
    elif len(p) == 4:
        p[0] = p[1]
        k, v = p[3]
        p[0][k] = v
    else:
        raise NotImplementedError(len(p))


def p_empty(p):
    """
    empty   : '{' '}'
    """
    p[0] = None


def p_kv(p):
    """
    kv  : KW_ARCHIVE '=' dict
        | KW_ARCHIVE_HEADER '=' dict
        | KW_ARCHIVE_NAME '=' STRING
        | KW_TOC_LIST '=' list
        | KW_ROOT_FOLDER '=' dict
        | KW_FILES '=' list
        | KW_FOLDER_INFO '=' dict
        | KW_FOLDERS '=' list
        | KW_TOC_HEADER '=' dict
        | KW_ALIAS '=' STRING
        | KW_NAME '=' STRING
        | KW_ROOT_PATH '=' PATH
        | KW_STORAGE '=' NUMBER
        | KW_STORAGE '=' list
        | KW_FILE '=' STRING
        | KW_SIZE '=' NUMBER
        | KW_STORE '=' NUMBER
        | KW_MAX_SIZE '=' NUMBER
        | KW_MIN_SIZE '=' NUMBER
        | KW_WILDCARD '=' STRING
        | KW_FOLDER '=' STRING
        | KW_PATH '=' PATH
        | NAME '=' NUMBER
        | NAME '=' PATH
        | NAME '=' STRING
        | NAME '=' dict
        | NAME '=' list
    """
    p[0] = p[1], p[3]


# Build the lexer
def build(**kwargs) -> LRParser:
    return yacc.yacc(**kwargs)
