#coding: utf-8

# validadores para tabelas
# computations
# form widgets
# visibility
# campos virtuais
# funcoes de validators
# validadores customizados


# esconder campos da tabela
def hide_fields(tablename, fields):
     for field in fields:
          db[tablename][field].writable = \
               db[tablename][field].readable = False