#!/usr/bin/env python

"""
A function to change the number into a text
"""

def resolve(df_cataloge, numberToResolve, cataloge, columnDesc='DESCRIPCIÓN', columnKey='CLAVE'):
    ''' Generic function to resolve a number to the given name which is in the descriptor cataloge'''
    try:
        # .ilco[0] for the very first element independet from the index
        return df_cataloge[cataloge][df_cataloge[cataloge][columnKey] == numberToResolve][columnDesc].iloc[0]
    except IndexError:
        print("Could not resolve {} in the given cataloge: {} with columDesc: {} and columnKey: {}".format(numberToResolve, cataloge, columnDesc, columnKey))
        return "ERROR - Check Resolve Function"

def resolveGender(df_cataloge, gender, cataloge="Catálogo SEXO"):
    return resolve(df_cataloge=df_cataloge,
                   numberToResolve=gender,
                   cataloge=cataloge)

def resolveState(df_cataloge, stateNumber, cataloge="Catálogo de ENTIDADES"):
    return resolve(df_cataloge=df_cataloge,
                  numberToResolve=stateNumber,
                  cataloge=cataloge,
                  columnKey='CLAVE_ENTIDAD',
                  columnDesc='ENTIDAD_FEDERATIVA')

