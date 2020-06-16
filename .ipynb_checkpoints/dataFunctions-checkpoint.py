#!/usr/bin/env python

"""
A set of Functions for the covid data
"""

def getPendingCasesDf(df, desc=3, column="RESULTADO"):
    ''' Returns a dataframe of all pending cases'''
    return df[df[column] == desc]
    
def getNegativeCasesDf(df, desc=2, column="RESULTADO"):
    ''' Returns a dataframe of all negative Cases'''
    return df[df[column] == desc]

def getPositiveCasesDf(df, desc=1, column="RESULTADO"):
    ''' Returns a dataframe of all positve Cases'''
    return df[df[column] == desc]

def getCasesPerAgeGroup(df, startAge, endAge, column="EDAD"):
    ''' Returns the number of cases of the given age range '''
    if endAge == -1:
        df_ageGroup = df[df[column] >= startAge]
    else:
        ageRange = list(range(startAge, endAge+1)) # +1 because it does not include the last number
        df_ageGroup = df[df[column].isin(ageRange)]
    return len(df_ageGroup.index)
    
def getNumberOfTotalCases(df):
    ''' Returns the number of total cases for the given dataframe '''
    totalCases = len(df.index)
    return totalCases

def getCasesPerState(df, column="ENTIDAD_RES"):
    ''' Returns a list of tuples with the state name and amount of cases
    
    @Return List[Tuple[StateName, SumCases]]
    '''
    statesAndCases = []
    for stateNumber in df[column].unique(): # loop through all states
        df_state = (df[df[column] == stateNumber])
        statesAndCases.append((stateNumber, len(df_state.index)))
    return statesAndCases

def getCasesPerSex(df, column="SEXO"):
    ''' Returns a list of tuples with the gender and the amount of cases
    
    @Return List[Tuple[Gender, SumCases]]
    '''
    genderAndCases = []
    for gender in df[column].unique():
        df_gender = df[df[column] == gender]
        genderAndCases.append((gender, len(df_gender.index)))
    return genderAndCases

def printHeading(heading):
    print("\n\n####################################################")
    print(heading)
    print("----------------------------------------------------")