
#Função para diagnóstico dos dados carregados

def diagnostico(df, nome="DataFrame"):
    """
    Mostra um relatório completo de qualidade dos dados.
    Use sempre antes de começar a limpeza!
    """
    print("=" * 55)
    print(f"  📊 DIAGNÓSTICO: {nome}")
    print("=" * 55)
    print(f"  Linhas:           {df.shape[0]:,}")
    print(f"  Colunas:          {df.shape[1]}")
    print(f"  Linhas duplicadas:{df.duplicated().sum():,}")
    print()
    
    nulos = df.isnull().sum()
    pct   = (nulos / len(df) * 100).round(1)
    
    print("  Coluna           | Tipo       | Nulos | % Nulos")
    print("  " + "-"*50)
    for col in df.columns:
        tipo = str(df[col].dtype)
        print(f"  {col:<18}| {tipo:<10} | {nulos[col]:<5} | {pct[col]}%")
    print("=" * 55)



