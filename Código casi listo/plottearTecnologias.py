# -*- coding: utf-8 -*-
"""
Created on Fri May 20 10:08:37 2022

@author: Carlos
"""

import pandas as pd
import re


def obtener_tecnologias():
    df = pd.read_csv('glassdoor_jobs.csv')

    tecno = df["Job Description"].apply(lambda x: x.split("knowledge",1)[1] if "knowledge" in x else( x.split("Knowledge",1)[1] if "Knowledge" in x else( x.split("KNOWLEDGE",1)[1] if "KNOWLEDGE" in x else (x.split("experience",1)[1] if "experience" in x else(x.split("Experience",1)[1] if "Experience" in x else(x.split("EXPERIENCE",1)[1] if "EXPERIENCE" in x else (x.split("skills",1)[1] if "skills" in x else(x.split("Skills",1)[1] if "Skills" in x else(x.split("SKILLS",1)[1] if "SKILLS" in x else (x.split("tools",1)[1] if "tools" in x else(x.split("Tools",1)[1] if "Tools" in x else(x.split("TOOLTS",1)[1] if "TOOLS" in x else (x.split("requirements",1)[1] if "requirements" in x else(x.split("Requirements",1)[1] if "Requirements" in x else(x.split("REQUERIMENTS",1)[1] if "REQUERIMENTS" in x else "NaD")))))))))))))))

    df["Job Description"] = tecno

    frames = []
    for i in range (df["Job Description"].shape[0]):
        if (df["Job Description"].loc[i]) != "NaD":
                res = re.findall(r'\w+', df["Job Description"].loc[i] )
                df1 = pd.DataFrame(res)
                frames.append(df1)

    result = pd.concat(frames)
    result_f = result.value_counts()

    result_f = pd.DataFrame(result_f)
    result_f = result_f.rename(columns={0:'Repeticiones'})
    result_f = result_f.reset_index()
    result_f = result_f.rename(columns={0:'Palabras'})



    with open("tecnologias.txt") as file_object:
        lines = file_object.readlines()
        lines = list(map(lambda x: x.rstrip('\n'),lines))
    lines = pd.DataFrame(lines)
    lines = lines.rename(columns={0:'Tecnologias'})


    lista_frec = []
    lista_tecno = []
    for line in range (lines['Tecnologias'].shape[0]):
        for j in range (result_f["Palabras"].shape[0]):
            if (result_f.loc[j,'Palabras']) == lines.loc[line,'Tecnologias']:
                lista_frec.append(result_f.loc[j,'Repeticiones'])
                lista_tecno.append(result_f.loc[j,'Palabras'])
                
                   

    df_t = pd.DataFrame()
    df_t['Tecnologia'] = lista_tecno
    df_t['Frecuencia'] = lista_frec
    df_t = df_t.sort_values(by = ['Frecuencia'], ascending = False)
    df_t = df_t.reset_index()
    df_t.drop(['index'], axis = 1, inplace = True)
    df_t = df_t.drop(df_t.index[[df_t.index > 4]])
    df_t.to_csv('LT.csv',index = False)