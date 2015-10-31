__author__ = 'marcelo'
import os

VERSION = 'Version beta 1.0'
CHANGE = 0

class variable():
    # base less
    color = ''
    bg_color = ''
    form_color = ''
    lk_color = ''
    social_color = ''

    def compile(self, entrada, saida, nome):

        style = open(os.path.abspath(entrada), 'r')
        clean = ''

        """  remove comments """
        for i in style.readlines():
            if str(entrada).split('.')[1] != 'html':
                try:
                    comment = i.split('/*')[1].split('*/')[0]
                    clean += i.replace('/*'+ comment+ '*/', '')
                except:
                    try:
                        comment = i.split('/**')[1].split('*/')[0]
                        clean += i.replace('/**'+ comment+ '*/', '')
                    except:
                        try:
                            comment = i.split('//')[1]
                            clean += i.replace('//'+ comment, '')
                        except:
                            try:
                                comment = i.split('/**')[1].split('**/')[0]
                                clean += i.replace('/**'+ comment+ '**/', '')
                            except:
                                clean += i
            else:
                try:
                    comment = i.split('<!--')[1].split('-->')[0]
                    clean += i.replace('<!--'+ comment+ '-->', '')
                except:
                    clean += i

        texto = clean

        """  variable base less"""
        if nome == 'base':
            if CHANGE == 1:
                self.color = 'color:#ff00ee'
                self.bg_color = 'background:#ff00ee'
                self.lk_color = 'color:#fff'
                self.social_color = 'color:#ff00ee'
                self.form_color = '#ff00ee'
            elif CHANGE == 2:
                self.color = 'color:#00eeff'
                self.bg_color = 'background:#00eeff'
                self.lk_color = 'color:#666'
                self.social_color = 'color:#00eeff'
                self.form_color = '#00eeff'
            else:
                self.color = 'color:#00ff00'
                self.bg_color = 'background:#00ff00'
                self.lk_color = 'color:#666'
                self.social_color = 'color:#00ff00'
                self.form_color = '#00ff00'

            texto = texto.replace('@color', self.color)
            texto = texto.replace('@bg_color', self.bg_color)
            texto = texto.replace('@lk_color', self.lk_color)
            texto = texto.replace('@social_color', self.social_color)
            texto = texto.replace('@form_color', self.form_color)

        """    minification   """
        if str(entrada).split('.')[1] != 'html':
            texto = texto.replace(' { ', '{')
            texto = texto.replace(' {', '{')
            texto = texto.replace(' }', '}')
            texto = texto.replace('} ', '}')
            texto = texto.replace('{ ', '{')
            texto = texto.replace('; }', ';}')
            texto = texto.replace(' ;', ';')
            texto = texto.replace('; ', ';')
            texto = texto.replace('[ ', '[')
            texto = texto.replace(' ]', ']')
            texto = texto.replace(' [', '[')
            texto = texto.replace('] ', ']')
            texto = texto.replace(', ', ',')
            texto = texto.replace(' , ', ',')
            texto = texto.replace(' = ', '=')
            texto = texto.replace(' == ', '==')
            texto = texto.replace(' ==', '==')
            texto = texto.replace('== ', '==')
            texto = texto.replace(' () {', '(){')
            texto = texto.replace('() {', '(){')
            texto = texto.replace(' (', '(')
            texto = texto.replace(': ', ':')
        texto = texto.replace('  ', '')
        if str(entrada).split('.')[1] != 'html':
            texto = texto.replace('var ', '')
            texto = texto.replace(' if', 'if')
            texto = texto.replace('if ', 'if')
            texto = texto.replace('else ', 'else')
            texto = texto.replace(' else', 'else')
            texto = texto.replace(' for', 'for')
            texto = texto.replace('for ', 'for')
            texto = texto.replace(' while', 'while')
            texto = texto.replace('while ', 'while')
            texto = texto.replace(' switch', 'switch')
            texto = texto.replace('switch ', 'switch')
            texto = texto.replace('do {', 'do{')
            texto = texto.replace(' do {', 'do{')
            texto = texto.replace('; }', ';}')
            texto = texto.replace(' $', '$')
        if str(entrada).split('.')[1] != 'html':
            texto = texto.replace(' <', '<')
            texto = texto.replace('< ', '<')
            texto = texto.replace(' < ', '<')
            texto = texto.replace('> ', '>')
            texto = texto.replace(' >', '>')
            texto = texto.replace('<= ', '<=')
            texto = texto.replace(' <=', '<=')
            texto = texto.replace(' <= ', '<=')
            texto = texto.replace(' >= ', '>=')
            texto = texto.replace(' >=', '>=')
            texto = texto.replace('>= ', '>=')
            texto = texto.replace(' != ', '!=')
            texto = texto.replace('!= ', '!=')
            texto = texto.replace(' !=', '!=')
            texto = texto.replace(': \'', ':\'')
            texto = texto.replace('\' ,', '\',')
            texto = texto.replace('+ \'', '+\'')
            texto = texto.replace(' && ', '&&')
            texto = texto.replace(' || ', '||')
        texto = texto.replace('\n', '')
        if str(entrada).split('.')[1] != 'html':
            texto = texto.replace('; }', ';}')

        """ remove comment multlines """
        if str(entrada).split('.')[1] != 'html':
            try:
                comment = texto.split('/**')[1].split('**/')[0]
                texto = texto.replace('/**'+ comment+ '**/', '')
            except:
                try:
                    comment = texto.split('/*')[1].split('*/')[0]
                    texto += texto.replace('/*'+ comment+ '*/', '')
                except:
                    texto += i

        """ variable js   """
        if str(entrada).split('.')[1] == 'js':
            texto = texto.replace('@form_color', self.form_color)

        style.close()
        novofile = open(os.path.abspath(saida), 'w+')
        novofile.write(texto)
        novofile.close()
