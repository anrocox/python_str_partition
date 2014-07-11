#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 10, 2014

@author: anroco

In python how to split a string into two using a string as separator?

En python ¿como dividir un string en dos teniendo en cuenta un caracter
separador?
'''

#create a str
s = 'I thought a thought. But the thought I thought.'
print(s)

#generates a tuple containing the part before the separator, the first
#separator itself and the part after the separator.
tupla = s.partition('.')
print(tupla)

#If the separator is not found, return a tuple containing the string itself,
#followed by two empty strings.
tupla = s.partition(',')
print(tupla)
