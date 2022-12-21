# Importation des bibliothèques
# Importation de la bibliothèque Pandas
import pandas as pd
# Importation des bibliothèques Matplotlib et Seaborn pour la visualisation des données
import matplotlib.pyplot as plt
import seaborn as sns
# Importation du dataset
# Importation du dataset dans un dataframe
df= pd.read_csv('FIFA.csv')
# Autrement
filename = 'FIFA.csv'
df = pd.read_csv(filename)
# Opérations sur le dataframe
# Afficher les données importées: Afficher l’ensemble des colonnes et des lignes du dataset.
print(df)
# Afficher les cinq premières lignes du dataset
print(df.head())
# Afficher les cinq dernières lignes du dataset
print(df.tail())
# Afficher les dix premières lignes du dataset
print(df.head(10))
# Afficher les dix dernières lignes du dataset
print(df.tail(10))
# Enumérer les colonnes du dataset
print(df.columns)
# Afficher le nombre de colonnes
print (len(df.columns))
 # Afficher les informations sur les données
2
print (df.info())
# Afficher un sommaire statistiques des données numériques (nombres de valeurs, moyenne, écart-
# type, ...), mais uniquement sur les colonnes numériques (faire df.describe(include = 'all') pour avoir
# toutes les colonnes) :
print(df.describe())
# Afficher la dimension du dataframe sous forme d’ un tuple de valeurs (nombre de lignes et nombre
# de colonnes )
print(df.shape)
# Vérifier si le dataframe contient des valeurs null. Renvoie un booléen, True ou False
print(df.isnull().any().any())
# Afficher les colonnes ayant des valeurs nulles
print(df.isnull().any())
# Afficher le nombre total des valeurs nulles
print(df.isnull().sum().sum())
# Afficher le nombre total des valeurs nulles pour chaque colonne
print(df.isnull().sum())
# Afficher les noms des joueurs, leurs scores triés dans l’ordre décroissant des scores
print(df[['Name','Overall']].sort_values(by='Overall',ascending=False))
# Afficher le noms et les scores des 5 meilleurs joueurs
print(df[['Name','Overall']].sort_values(by='Overall',ascending=False).head())
# Top 5 pays des meilleurs joueurs
print(df[['Name','Nationality','Overall']].sort_values(by='Overall',ascending=False).head())
# Top 5 clubs des meilleurs joueurs
print(df[['Name','Club','Overall']].sort_values(by='Overall',ascending=False).head())
# Afficher les salaires (Wage : sous format €130K ) : Les 5 meilleurs salaires des joueurs
df.Wage=df.Wage.str.replace('€','')
df.Wage=df.Wage.str.replace('K','').astype('float')
print(df[['Name','Wage']].sort_values(by='Wage',ascending=False).head())
# Age minimum : Afficher Les colonnes Name et Age des lignes ayant l’âge minimum
print("Minimum Age:",df['Age'].min())
min=df['Age'].min()
print (df[df.Age==min][['Name','Age']])
# Age maximum : Afficher Les colonnes Name et Age des lignes ayant l’âge maximum
print("Maximum Age:",df['Age'].max())
max=df['Age'].max()
print (df[df.Age==max][['Name','Age']])
# Visualisation des données
# Top 5 des nationalités
# Le nombre de joueurs de chaque nationalité
print(df['Nationality'].value_counts())
# Le nombre de joueurs des 5 plus fréquentes nationalités
print(df['Nationality'].value_counts().head())
# Les 5 plus fréquentes nationalités
print(df['Nationality'].value_counts().head().keys())
# Création du bar plot des cinq premières lignes
abscisse=list(df['Nationality'].value_counts().head().keys())
ordonne=list(df['Nationality'].value_counts().head())
plt.bar(abscisse, ordonne, color ='cyan',width = 0.6)
plt.xlabel("Nationalites")
plt.ylabel("Effectif")
3
plt.title("Effectif des joueurs en fonction des Nationalites")
plt.show()
plt.close
# Autrement
plt.bar(list(df['Nationality'].value_counts().head().keys()), list(df['Nationality'].value_counts().head()))
# On peut faire la même chose pour visualiser les nationalités les moins fréquentes : Utiliser tail à la
# place de head
# les différentes positions acquises par les joueurs
# matplotlib.pyplot.figure (figsize(float, float)), default: rcParams["figure.figsize"] (default: [6.4, 4.8])
# Width, height in inches.
plt.figure(figsize = (18, 8)) # Width, height in inches.
plt.style.use('fivethirtyeight')
abscisse=list(df['Position'].value_counts().keys())
ordonnee=list(df['Position'].value_counts())
plt.bar(abscisse, ordonnee, color ='yellow',edgecolor = 'red',width = 0.7)
plt.xlabel("Different Positions in Football")
plt.ylabel("Count of Players")
plt.title("Players Positions")
plt.show()
plt.close()
# Afficher un histogramme Age vs Overall
plt.figure(figsize=(10,5))
sns.barplot(x='Age',y='Overall',data=df)
# Afficher un histogramme pour chaque valeur unique (Left, Right) de la colonne 'Preferred Foot'
plt.rcParams['figure.figsize'] = (10, 5) # changer les valeurs par défaut
sns.countplot(df['Preferred Foot'], palette = 'pink')
plt.title('Most Preferred Foot of the Players', fontsize = 20)
plt.show()
plt.close()
# Si on veut vérifier les valeurs :
print(df['Preferred Foot'].unique()) # les valeurs uniques de la colonne 'Preferred Foot'
print(df['Preferred Foot'].value_counts(sort=False)) # Afficher le nombre pour chaque valeur
# Comparaison des salaires des joueurs : visualiser la distribution des salaires
df.Wage=df.Wage.str.replace('€','')
df.Wage=df.Wage.str.replace('K','').astype('float')
plt.rcParams['figure.figsize'] = (10, 5)
sns.distplot(df['Wage'], color = 'blue')
plt.xlabel('Wage Range for Players', fontsize = 16)
plt.ylabel('Count of the Players', fontsize = 16)
plt.title('Distribution of Wages of Players', fontsize = 20)
plt.show()
plt.close() 