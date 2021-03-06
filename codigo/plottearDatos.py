import pandas as pd
import matplotlib.pyplot as plt



def plottear_salario(df):

    dfDatos = pd.DataFrame(df['Salario Mensual'])
    dfDatos2 = dfDatos.groupby('Salario Mensual')['Salario Mensual'].count()
    tplot = dfDatos.groupby('Salario Mensual')['Salario Mensual'].count().plot(
        xlabel="Salario mensual estimado", ylabel="Cantidad de ofertas", color="darkorange", kind='bar', title="Cantidad de ofertas por salario mensual estimado", legend=False)
    tplot.annotate('Total de ofertas: '+str(dfDatos2.sum()),
                   xy=(dfDatos2.count()*.7, dfDatos2.max()*.8), ha='center', va='bottom')
    for p in tplot.patches:
        tplot.annotate(str(p.get_height()), xy=(
            (p.get_x()), p.get_height()), ha='left', va='bottom')

    plt.savefig('testplot.png', dpi=300, bbox_inches='tight')
    plt.close()


def plottear_modalidad(df):

    dfDatos = pd.DataFrame(df['Modalidad'])
    dfDatos2 = dfDatos.groupby('Modalidad')['Modalidad'].count()
    tplot = dfDatos.groupby('Modalidad')['Modalidad'].count().plot(xlabel="Tipo de modalidad", ylabel="Cantidad de ofertas",
                                                                   color="darkorange", kind='bar', title="Cantidad de ofertas por modalidad de trabajo", width=.2, legend=False)
    tplot.annotate('Total de ofertas: '+str(dfDatos2.sum()),
                   xy=(dfDatos2.count()*.5, dfDatos2.max()*.8), ha='center', va='bottom')
    for p in tplot.patches:
        tplot.annotate(str(p.get_height()), xy=(
            (p.get_x()), p.get_height()), ha='left', va='bottom')

    plt.xticks(rotation=360)
    plt.savefig('testplot.png', dpi=300, bbox_inches='tight')
    plt.close()


def plottear_tamano_empresa(df):

    dfDatos = pd.DataFrame(df['Tamaño Empresa'])
    dfDatos2 = dfDatos.groupby('Tamaño Empresa')['Tamaño Empresa'].count()
    tplot = dfDatos.groupby('Tamaño Empresa')['Tamaño Empresa'].count().plot(xlabel="Tamaño de empresa", ylabel="Cantidad de ofertas",
                                                                             color="darkorange", kind='bar', title="Cantidad de ofertas por tamaño de la empresa", width=.2, legend=False)
    tplot.annotate('Total de ofertas: '+str(dfDatos['Tamaño Empresa'].count()), xy=(
        dfDatos2.count()*.5, dfDatos2.max()*.8), ha='center', va='bottom')
    for p in tplot.patches:
        tplot.annotate(str(p.get_height()), xy=(
            (p.get_x()), p.get_height()), ha='left', va='bottom')

    plt.savefig('testplot.png', dpi=300, bbox_inches='tight')
    plt.close()


def plottear_locacion(df):

    dfDatos = pd.DataFrame(df['Locacion'])
    dfDatos2 = dfDatos.groupby('Locacion')['Locacion'].count()
    tplot = dfDatos.groupby('Locacion')['Locacion'].count().plot(xlabel="Locacion", ylabel="Cantidad de ofertas",
                                                                 color="darkorange", kind='bar', title="Cantidad de ofertas por locacion en México del trabajo", width=.6, legend=False)
    tplot.annotate('Total de ofertas: '+str(dfDatos2.sum()),
                   xy=(dfDatos2.count()*.7, dfDatos2.max()*.8), ha='center', va='bottom')
    tplot.set_yscale('log')
    for p in tplot.patches:
        tplot.annotate(str(p.get_height()), xy=(
            (p.get_x()), p.get_height()), ha='left', va='bottom')

    plt.savefig('testplot.png', dpi=300, bbox_inches='tight')
    plt.close()


def plottear_tecnologias(df_t):
    plt.bar(df_t['Tecnologia'], df_t['Frecuencia'], color="darkorange")

    for i in range(df_t.shape[0]):
        plt.annotate(df_t.loc[i, 'Frecuencia'], xy=(
            df_t.loc[i, 'Tecnologia'], (df_t.loc[i, 'Frecuencia']+4)), ha='center')

    plt.title('Frecuencia de aparicion de las tecnologias en las ofertas de trabajo')
    plt.ylabel('Frecuencia en las ofertas de trabajo')
    plt.xlabel('Tecnologias')
    plt.savefig('tecno.png', dpi=300, bbox_inches='tight')
    plt.close()


def plottear_modalidad_EG(CMT):

    plt.bar(CMT['Modalidad'], CMT['Empresa Grande'],
            color="darkorange", width=.35)

    for i in range(CMT.shape[0]):
        plt.annotate(CMT.loc[i, 'Empresa Grande'], xy=(
            CMT.loc[i, 'Modalidad'], (CMT.loc[i, 'Empresa Grande']+5)), ha='center')

    plt.title('Cantidad de ofertas por modalidad en empresas grandes')
    plt.ylabel('Cantidad de ofertas')
    plt.xlabel('Modalidad')
    plt.annotate('Total de ofertas: ' + CMT['Total de ofertas Grande'].loc[0], xy=(
        ('Virtual'), CMT['Empresa Grande'].loc[0] - 20), ha='center')
    plt.savefig('testplot.png', dpi=300, bbox_inches='tight')
    plt.close()


def plottear_modalidad_EM(CMT):

    plt.bar(CMT['Modalidad'], CMT['Empresa Mediana'],
            color="darkorange", width=.35)

    for i in range(CMT.shape[0]):
        plt.annotate(CMT.loc[i, 'Empresa Mediana'], xy=(
            CMT.loc[i, 'Modalidad'], (CMT.loc[i, 'Empresa Mediana']+3)), ha='center')

    plt.title('Cantidad de ofertas por modalidad en empresas medianas')
    plt.ylabel('Cantidad de ofertas')
    plt.xlabel('Modalidad')
    plt.annotate('Total de ofertas: ' + CMT['Total de ofertas Mediana'].loc[0], xy=(
        'Virtual', CMT['Empresa Mediana'].loc[0] - 20), ha='center')
    plt.savefig('testplot.png', dpi=300, bbox_inches='tight')
    plt.close()


def plottear_modalidad_EP(CMT):

    plt.bar(CMT['Modalidad'], CMT['Empresa Pequena'],
            color="darkorange", width=.35)

    for i in range(CMT.shape[0]):
        plt.annotate(CMT.loc[i, 'Empresa Pequena'], xy=(
            CMT.loc[i, 'Modalidad'], (CMT.loc[i, 'Empresa Pequena']+0.5)), ha='center')

    plt.title('Cantidad de ofertas por modalidad en empresas pequeñas')
    plt.ylabel('Cantidad de ofertas')
    plt.xlabel('Modalidad')
    plt.annotate('Total de ofertas: ' + CMT['Total de ofertas Pequena'].loc[0], xy=(
        'Virtual', CMT['Empresa Pequena'].loc[0] - 5), ha='center')
    plt.savefig('testplot.png', dpi=300, bbox_inches='tight')
    plt.close()


def plottear_locacion_EG(CLT):

    sumatoria_grande = CLT['Repeticiones'].sum()

    plt.bar(CLT['Locaciones'], CLT['Repeticiones'], color="darkorange")
    plt.xticks(rotation=90)

    for i in range(CLT.shape[0]):
        plt.annotate(CLT.loc[i, 'Repeticiones'], xy=(
            CLT.loc[i, 'Locaciones'], (CLT.loc[i, 'Repeticiones']+5)), ha='center')

    plt.title('Cantidad de ofertas por locación en empresas grandes')
    plt.ylabel('Cantidad de ofertas')
    plt.xlabel('Locación')
    plt.annotate('Total de ofertas = %i' % sumatoria_grande, xy=(
        CLT['Locaciones'].loc[i-1], CLT['Repeticiones'].loc[0]-10))
    plt.savefig('testplot.png', dpi=300, bbox_inches='tight')
    plt.close()


def plottear_locacion_EM(CLTM):
    sumatoria_mediana = CLTM['Repeticiones'].sum()

    plt.bar(CLTM['Locaciones'], CLTM['Repeticiones'], color="darkorange")
    plt.xticks(rotation=90)

    for i in range(CLTM.shape[0]):
        plt.annotate(CLTM.loc[i, 'Repeticiones'], xy=(
            CLTM.loc[i, 'Locaciones'], (CLTM.loc[i, 'Repeticiones']+5)), ha='center')

    plt.title('Cantidad de ofertas por locación en empresas medianas')
    plt.ylabel('Cantidad de ofertas')
    plt.xlabel('Locación')
    plt.annotate('Total de ofertas = %i' % sumatoria_mediana, xy=(
        CLTM['Locaciones'].loc[i-1], CLTM['Repeticiones'].loc[0]-10), ha='center')
    plt.savefig('testplot.png', dpi=300, bbox_inches='tight')
    plt.close()


def plottear_locacion_EP(CLTP):
    sumatoria_pequena = CLTP['Repeticiones'].sum()

    plt.bar(CLTP['Locaciones'], CLTP['Repeticiones'], color="darkorange")
    plt.xticks(rotation=90)

    for i in range(CLTP.shape[0]):
        plt.annotate(CLTP.loc[i, 'Repeticiones'], xy=(
            CLTP.loc[i, 'Locaciones'], (CLTP.loc[i, 'Repeticiones']+0.2)), ha='center')

    plt.title('Cantidad de ofertas por locación en empresas pequeñas')
    plt.ylabel('Cantidad de ofertas')
    plt.xlabel('Locación')
    plt.annotate('Total de ofertas = %i' % sumatoria_pequena, xy=(
        CLTP['Locaciones'].loc[i-1], CLTP['Repeticiones'].loc[0]-3), ha='center')
    plt.savefig('testplot.png', dpi=300, bbox_inches='tight')
    plt.close()


def plottear_TE_vir(CTM):

    plt.bar(CTM['Tamaño de empresa'], CTM['Virtual'], color="darkorange")

    for i in range(CTM.shape[0]):
        plt.annotate(CTM.loc[i, 'Virtual'], xy=(
            CTM.loc[i, 'Tamaño de empresa'], (CTM.loc[i, 'Virtual'])+0.03), ha='center')

    plt.title('Cantidad de ofertas por tamaño de empresa en modalidad virtual')
    plt.ylabel('Cantidad de ofertas')
    plt.xlabel('Tamaño de empresa')
    plt.annotate('Total de ofertas: ' + CTM['Total de ofertas Presencial'].loc[0], xy=(
        'Pequeña', CTM['Virtual'].loc[0]-0.25), ha='center')
    plt.savefig('testplot.png', dpi=300, bbox_inches='tight')
    plt.close()


def plottear_TE_pres(CTM):

    plt.bar(CTM['Tamaño de empresa'], CTM['Presencial'], color="darkorange")

    for i in range(CTM.shape[0]):
        plt.annotate(CTM.loc[i, 'Presencial'], xy=(
            CTM.loc[i, 'Tamaño de empresa'], (CTM.loc[i, 'Presencial']+5)), ha='center')

    plt.title('Cantidad de ofertas por tamaño de empresa en modalidad presencial')
    plt.ylabel('Cantidad de ofertas')
    plt.xlabel('Tamaño de empresa')
    plt.annotate('Total de ofertas: ' + CTM['Total de ofertas Presencial'].loc[0], xy=(
        'Pequeña', CTM['Presencial'].loc[0] - 20), ha='center')
    plt.savefig('testplot.png', dpi=300, bbox_inches='tight')
    plt.close()


def plottear_salario_eg(df):

    dfDatos = df
    dfDatos2 = dfDatos.groupby('Tamaño Empresa')['Salario Mensual'].sum()
    dfDatos2.columns = ['Tamaño Empresa', 'Suma']
    dfDatos3 = dfDatos.groupby('Tamaño Empresa')['Salario Mensual'].count()
    dfDatos2.columns = ['Tamaño Empresa', 'Cantidd']

    df4 = pd.DataFrame()
    df4 = pd.concat([dfDatos2, dfDatos3], axis=1)
    df4.columns = ['Suma', 'Cantidad']

    df4 = pd.DataFrame()
    df4 = pd.concat([dfDatos2, dfDatos3], axis=1)
    df4.columns = ['Suma', 'Cantidad']

    df4['Promedio'] = df4['Suma'] / df4['Cantidad']

    salarioint = df4['Promedio'].apply(lambda x: int(x))
    df4['Promedio'] = salarioint

    dfsalario_grande_ambos = pd.DataFrame(df4['Promedio'])
    df4['Cantidad']['Pequeña'] = 0
    # df4['Cantidad']['Mediana'] = 0 decomentar si hay ofertas de empresas medianas

    # .drop(['Mediana']) decomentar si hay ofertas de empresas medianas
    dfsalario_grande = dfsalario_grande_ambos.drop(['Pequeña'])
    tplot = dfsalario_grande.plot(xlabel="Tamaño", ylabel="Salario en pesos", color="darkorange",
                                  kind='bar', title="Salario promedio por empresas grandes en México", width=.05, legend=False)
    tplot.annotate('Total de ofertas: '+str(df4['Cantidad'].sum(
    )), xy=(.2, df4['Promedio'].max()*.8), ha='center', va='bottom', fontsize=8)
    for p in tplot.patches:
        tplot.annotate(str(p.get_height()), xy=(
            (p.get_x()), p.get_height()), ha='left', va='bottom')

    plt.xticks(rotation=360)
    plt.savefig('testplot.png', dpi=300, bbox_inches='tight')
    plt.close()


def plottear_salario_em(df):

    dfDatos = df
    dfDatos2 = dfDatos.groupby('Tamaño Empresa')['Salario Mensual'].sum()
    dfDatos2.columns = ['Tamaño Empresa', 'Suma']
    dfDatos3 = dfDatos.groupby('Tamaño Empresa')['Salario Mensual'].count()
    dfDatos2.columns = ['Tamaño Empresa', 'Cantidd']

    df4 = pd.DataFrame()
    df4 = pd.concat([dfDatos2, dfDatos3], axis=1)
    df4.columns = ['Suma', 'Cantidad']

    df4 = pd.DataFrame()
    df4 = pd.concat([dfDatos2, dfDatos3], axis=1)
    df4.columns = ['Suma', 'Cantidad']

    df4['Promedio'] = df4['Suma'] / df4['Cantidad']

    salarioint = df4['Promedio'].apply(lambda x: int(x))
    df4['Promedio'] = salarioint

    dfsalario_grande_ambos = pd.DataFrame(df4['Promedio'])
    df4['Cantidad']['Pequeña'] = 0
    df4['Cantidad']['Grande'] = 0

    dfsalario_grande = dfsalario_grande_ambos.drop(
        ['Grande']).drop(['Mediana'])
    tplot = dfsalario_grande.plot(xlabel="Tamaño", ylabel="Salario en pesos", color="darkorange",
                                  kind='bar', title="Salario promedio por empresas medianas en México", width=.05, legend=False)
    tplot.annotate('Total de ofertas: '+str(df4['Cantidad'].sum()),
                   xy=(.2, df4['Promedio'].max()*.8), ha='center', va='bottom')
    for p in tplot.patches:
        tplot.annotate(str(p.get_height()), xy=(
            (p.get_x()), p.get_height()), ha='left', va='bottom')

    plt.xticks(rotation=360)
    plt.savefig('testplot.png', dpi=300, bbox_inches='tight')
    plt.close()


def plottear_salario_ep(df):

    dfDatos = df
    dfDatos2 = dfDatos.groupby('Tamaño Empresa')['Salario Mensual'].sum()
    dfDatos2.columns = ['Tamaño Empresa', 'Suma']
    dfDatos3 = dfDatos.groupby('Tamaño Empresa')['Salario Mensual'].count()
    dfDatos2.columns = ['Tamaño Empresa', 'Cantidd']

    df4 = pd.DataFrame()
    df4 = pd.concat([dfDatos2, dfDatos3], axis=1)
    df4.columns = ['Suma', 'Cantidad']

    df4 = pd.DataFrame()
    df4 = pd.concat([dfDatos2, dfDatos3], axis=1)
    df4.columns = ['Suma', 'Cantidad']

    df4['Promedio'] = df4['Suma'] / df4['Cantidad']

    salarioint = df4['Promedio'].apply(lambda x: int(x))
    df4['Promedio'] = salarioint

    dfsalario_grande_ambos = pd.DataFrame(df4['Promedio'])
    df4['Cantidad']['Grande'] = 0
    # df4['Cantidad']['Mediana'] = 0 decomentar si hay ofertas de empresas medianas

    # .drop(['Mediana']) descomentar si hay ofertas de empresas medianas con salario
    dfsalario_grande = dfsalario_grande_ambos.drop(['Grande'])
    tplot = dfsalario_grande.plot(xlabel="Tamaño", ylabel="Salario en pesos", color="darkorange",
                                  kind='bar', title="Salario promedio por empresas pequeñas en México", width=.05, legend=False)
    tplot.annotate('Total de ofertas: '+str(df4['Cantidad'].sum()),
                   xy=(.15, dfsalario_grande.max()*.8), ha='center', va='bottom')
    for p in tplot.patches:
        tplot.annotate(str(p.get_height()), xy=(
            (p.get_x()), p.get_height()), ha='left', va='bottom')

    plt.xticks(rotation=360)
    plt.savefig('testplot.png', dpi=300, bbox_inches='tight')
    plt.close()


def plottear_salario_presencial(df):

    dfDatos = df
    dfDatos2 = dfDatos.groupby('Modalidad')['Salario Mensual'].sum()
    dfDatos2.columns = ['Modalidad', 'Suma']
    dfDatos3 = dfDatos.groupby('Modalidad')['Salario Mensual'].count()
    dfDatos2.columns = ['Modalidad', 'Cantidd']

    df4 = pd.DataFrame()
    df4 = pd.concat([dfDatos2, dfDatos3], axis=1)
    df4.columns = ['Suma', 'Cantidad']

    df4 = pd.DataFrame()
    df4 = pd.concat([dfDatos2, dfDatos3], axis=1)
    df4.columns = ['Suma', 'Cantidad']

    df4['Promedio'] = df4['Suma'] / df4['Cantidad']

    salarioint = df4['Promedio'].apply(lambda x: int(x))
    df4['Promedio'] = salarioint

    dfsalario_grande_ambos = pd.DataFrame(df4['Promedio'])
    df4['Cantidad']['Virtual'] = 0

    dfsalario_grande = dfsalario_grande_ambos.drop(['Virtual'])
    tplot = dfsalario_grande.plot(xlabel="Modalidad", ylabel="Salario en pesos", color="darkorange",
                                  kind='bar', title="Salario promedio por modalidad presencial en México", width=.05, legend=False)
    tplot.annotate('Total de ofertas: '+str(df4['Cantidad'].sum()),
                   xy=(.15, dfsalario_grande.max()*.8), ha='center', va='bottom')
    for p in tplot.patches:
        tplot.annotate(str(p.get_height()), xy=(
            (p.get_x()), p.get_height()), ha='left', va='bottom')

    plt.xticks(rotation=360)
    plt.savefig('testplot.png', dpi=300, bbox_inches='tight')
    plt.close()


def plottear_salario_virtual(df):

    dfDatos = df
    dfDatos2 = dfDatos.groupby('Modalidad')['Salario Mensual'].sum()
    dfDatos2.columns = ['Modalidad', 'Suma']
    dfDatos3 = dfDatos.groupby('Modalidad')['Salario Mensual'].count()
    dfDatos2.columns = ['Modalidad', 'Cantidd']

    df4 = pd.DataFrame()
    df4 = pd.concat([dfDatos2, dfDatos3], axis=1)
    df4.columns = ['Suma', 'Cantidad']

    df4 = pd.DataFrame()
    df4 = pd.concat([dfDatos2, dfDatos3], axis=1)
    df4.columns = ['Suma', 'Cantidad']

    df4['Promedio'] = df4['Suma'] / df4['Cantidad']

    salarioint = df4['Promedio'].apply(lambda x: int(x))
    df4['Promedio'] = salarioint

    dfsalario_grande_ambos = pd.DataFrame(df4['Promedio'])
    df4['Cantidad']['Presencial'] = 0

    dfsalario_grande = dfsalario_grande_ambos.drop(['Presencial'])
    tplot = dfsalario_grande.plot(xlabel="Modalidad", ylabel="Salario en pesos", color="darkorange",
                                  kind='bar', title="Salario promedio por modalidad virtual en México", width=.05, legend=False)
    tplot.annotate('Total de ofertas: '+str(df4['Cantidad'].sum()),
                   xy=(.15, dfsalario_grande.max()*.8), ha='center', va='bottom')
    for p in tplot.patches:
        tplot.annotate(str(p.get_height()), xy=(
            (p.get_x()), p.get_height()), ha='left', va='bottom')

    plt.xticks(rotation=360)
    plt.savefig('testplot.png', dpi=300, bbox_inches='tight')
    plt.close()
