
#Imports : 
import streamlit as st
import pandas as pd
from skops.io import load
import folium
from streamlit_folium import st_folium

# Set the background image
background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://imagizer.imageshack.com/img922/387/pwfYCp.png");
    background-size: cover;
    background-position: center; 
    background-repeat: no-repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)


def onglet0(): 

    st.markdown("<h1 style='text-align: center; color: #227DA7;'>Data Analytics</h1>", unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.markdown("<h5 style='text-align: center; color: #012D47;'>Bienvenue dans notre application d'aide à la détection de maladies.</h5>", unsafe_allow_html=True)
    st.write("")

    personne = st.selectbox("Vous êtes ? ", ('', 'Un Particulier', 'Un Professionnel de santé'))

    if personne == 'Un Particulier' : 
        
        st.markdown("<h5 style='text-align: left; color: #012D47;'>Cher Patient,</h5>", unsafe_allow_html=True)
        st.write("Avec vos résultats d'analyses (sanguines, urines, physiques), que vous pourrez renseigner, il vous sera possible d'évaluer le risque (faible ou élevé) des maladies suivantes :")
        st.write("- Cancer du sein.")
        st.write("- Diabète.")
        st.write("- Maladie cardiaque.")
        st.write("- Maladie Rénale.")
        st.write("- Maladie du foie.")
        st.write("Vous pourrez télécharger un fichier CSV contenant vos résultats ou remplir les champs manuellement.")
        st.write("L'application traitera vos données et renverra la présence d'un risque faible ou élevé à la maladie.")
        st.markdown("<h6 style='text-align: left; color: #012D47;'>Cette analyse ne se substitue pas à un avis médical, nous vous conseillons de vous rapprocher d'un spécialiste.</h6>", unsafe_allow_html=True)
        st.write("Si vous n'avez pas encore de spécialiste vous avez la possibilité de cliquer sur 'Je souhaite trouver un spécialiste', de renseigner votre région et vous trouverez une carte pour vous orienter vers un spécialiste.")
    
    elif personne == 'Un Professionnel de santé' :
        
        st.markdown("<h5 style='text-align: left; color: #012D47;'>Cher Praticien,</h5>", unsafe_allow_html=True)
        st.write("Avec les résultats d'analyses (sanguines, urines, physiques) de vos patients, que vous pourrez renseigner, il vous sera possible d'évaluer le risque (faible ou élevé) des maladies suivantes :")
        st.write("- Cancer du sein.")
        st.write("- Diabète.")
        st.write("- Maladie cardiaque.")
        st.write("- Maladie Rénale.")
        st.write("- Maladie du foie.")
        st.write("Vous pourrez télécharger un fichier CSV (un fichier par maladie) contenant les résultats d'un ou plusieurs patients ou remplir les champs manuellement.")
        st.write("L'application traitera les données et renverra la présence d'un risque faible ou élevé à la maladie.")
        st.write("Si votre patient ne possède pas encore de spécialiste il vous est possible de cliquer sur 'Je souhaite trouver un spécialiste', de saisir une région et d'orienter, à partir de la carte, votre patient vers un spécialiste.")
    
    st.write("")
    st.write("Cette application a été développée par une équipe de Data Analyst dans le cadre d'un projet à but pédagogique.")
    st.write("Elle est basée sur des algorithmes entraînés pour identifier et prédire le risque de cinq maladies majeures.")


def onglet1():

    st.markdown("<h1 style='text-align: center; color: #227DA7;'>Cancer du sein</h1>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: left; color: #012D47;'>Entrer les résultats d'analyses du patient</h6>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: left; color: #012D47;'>En téléchargeant un fichier ou en remplissant les champs demandés.</h6>", unsafe_allow_html=True)

    background_image = """
    <img src = "https://www.fondation-arc.org/sites/default/files/styles/info_material_default/public/2022-09/ARC_Affiche_Cancer%20du%20sein_2022%20COUVERTURE%20copie.jpg.webp?itok=Cxy73jXV"
            width = "450px"
            height = "600px"/>
    """

    #st.markdown(background_image, unsafe_allow_html=True)

    Fichier = st.toggle('Télécharger un fichier')

    if Fichier : 

        liste_features = ['radius_mean', 'texture_mean', 'smoothness_mean', 'compactness_mean','concavity_mean', 'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean']
        uploaded_file = st.file_uploader("Choisissez un fichier au format .csv : ")
        if uploaded_file is not None:
            dataframe = pd.read_csv(uploaded_file)
            df = dataframe[liste_features]
            st.write('Vérifiez les données chargées : ')
            st.write(df)
            if st.button('Soumettre', key = 'soumettre_auto'):
                #Scalage des données et prédictions :
                scaler_sein = load("data_scaler.skops", trusted=True)
                algo_sein = load("data_algo.skops", trusted=True)
                scalage_auto = scaler_sein.transform(df)
                results_auto = algo_sein.predict(scalage_auto)
                        
                st.markdown("<h1 style='text-align: center; color: #227DA7;'>Résultats de l'analyse</h1>", unsafe_allow_html=True)
                if len(results_auto) == 1 : 
                    for final in results_auto:
                        if final == 1:
                            st.markdown("<h6 style='text-align: left; color: #012D47;'>Selon vos données renseignées, notre analyse indique que les cellules sont probablement des cellules malignes.</h6>", unsafe_allow_html=True)
                            st.markdown("<h6 style='text-align: left; color: #012D47;'>Cette analyse ne se substitue pas à un avis médical.</h6>", unsafe_allow_html=True)
                            st.markdown("<h6 style='text-align: left; color: #012D47;'>Si vous n'êtes pas médecin, Nous vous conseillons de vous rapprocher de votre spécialiste</h6>", unsafe_allow_html=True)
                        else:
                            st.markdown("<h6 style='text-align: left; color: #012D47;'>Selon vos données renseignées, notre analyse indique que les cellules sont probablement des cellules bénignes.</h6>", unsafe_allow_html=True)
                            st.markdown("<h6 style='text-align: left; color: #012D47;'>Cette analyse ne se substitue pas à un avis médical.</h6>", unsafe_allow_html=True)
                            st.markdown("<h6 style='text-align: left; color: #012D47;'>Si vous n'êtes pas médecin, Nous vous conseillons de vous rapprocher de votre spécialiste</h6>", unsafe_allow_html=True)
                else : 
                    df.insert(0, 'Résultats', results_auto)
                    df['Résultats'] = df['Résultats'].replace(0, 'Cellules potentiellement bénignes').replace(1, 'Cellules potentiellement malignes')
                    st.write(df)
                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Cette analyse ne se substitue pas à un avis médical.</h6>", unsafe_allow_html=True)
                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Si vous n'êtes pas médecin, Nous vous conseillons de vous rapprocher de votre spécialiste</h6>", unsafe_allow_html=True)

    Manu = st.toggle('Renseigner les champs')

    if Manu : 

        #Entrée des données patient :
        radius_mean = st.number_input("Entrer le rayon moyen (µm) (radius_mean) : ", value=None, placeholder="12,88")  # 1
        texture_mean = st.number_input("Entrer la texture moyenne (texture_mean) : ",  value=None, placeholder="29,92") # 2 
        smoothness_mean = st.number_input("Entrer le lissage moyen (smoothness_mean)",  value=None, placeholder="0,08123") # 3
        compactness_mean = st.number_input("Entrer la densité (compactness_mean) : ", value=None, placeholder="0,0582")# 4
        concavity_mean = st.number_input("Entrer la concavité moyenne (concavity_mean) : ", value=None, placeholder="0,062") # 5
        concave_points_mean = st.number_input("Entrer la valeur des points de concavité moyens (cocave_points_mean) : ", value=None, placeholder="0,0234") # 6
        symmetry_mean = st.number_input("Entrer la symétrie moyenne (symmetry_mean) : ", value=None, placeholder="0,1566") # 7
        fractal_dimension_mean = st.number_input("Entrer la dimension fractale moyenne (fractal_dimension_mean) : ", value=None, placeholder="0,0571")# 8
        
        #Prédictions : 
        if st.button('Soumettre', key = 'soumettre_manu'):
            #Scalage des données et algorithme : 
            scaler_sein = load("data_scaler.skops", trusted=True)
            algo_sein = load("data_algo.skops", trusted=True)
            scalage = scaler_sein.transform([[radius_mean, texture_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean]])
            results = algo_sein.predict(scalage)
            
            st.markdown("<h1 style='text-align: center; color: #227DA7;'>Résultats de l'analyse</h1>", unsafe_allow_html=True)
            for final in results:
                if final == 1:
                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Selon vos données renseignées, notre analyse indique que les cellules sont probablement des cellules malignes.</h6>", unsafe_allow_html=True)
                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Cette analyse ne se substitue pas à un avis médical.</h6>", unsafe_allow_html=True)
                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Si vous n'êtes pas médecin, Nous vous conseillons de vous rapprocher de votre spécialiste</h6>", unsafe_allow_html=True)
                else:
                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Selon vos données renseignées, notre analyse indique que les cellules sont probablement des cellules bénignes.</h6>", unsafe_allow_html=True)
                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Cette analyse ne se substitue pas à un avis médical.</h6>", unsafe_allow_html=True)
                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Si vous n'êtes pas médecin, Nous vous conseillons de vous rapprocher de votre spécialiste</h6>", unsafe_allow_html=True)

    Specialistes = st.toggle('Je souhaite trouver un spécialiste')

    if Specialistes : 

        #Chargement du dataframe des spécialiste : 
        data_spe = pd.read_csv('data_med.csv', sep=',')
        data_spe['Coordonnées'] = data_spe['Coordonnées'].apply(lambda x: list(map(float, x.split(','))))

        #Filtre du dataframe que pour la maladie : 
        data_sein = data_spe[data_spe['Profession'] == 'Cancérologue médical']

        #Choisir la région : 
        region = [""] + list(data_sein["Nom Officiel Région"].unique())
        region_user = st.selectbox("Sélectionnez une région",region)

        #Filtre du dataframe sur la région choisie : 
        df_region = data_sein[data_sein['Nom Officiel Région'] == region_user].reset_index(drop=True)

        #Création de la carte avec les spécialistes : 
        if region_user != '' : 

            m = folium.Map(location=df_region['Coordonnées'][0], zoom_start=8)
            for index, row in df_region.iterrows():
                folium.Marker(location=row['Coordonnées'], popup=row[['Nom du professionnel','Adresse','Numéro de téléphone']]).add_to(m)
            st_map = st_folium(m, width=700,height=450)
            
        else : 
            st.write('Veuillez sélectionner une région')

def onglet2():
    
    st.markdown("<h1 style='text-align: center; color: #227DA7;'>Diabète</h1>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: left; color: #012D47;'>Entrer les résultats d'analyses du patient</h6>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: left; color: #012D47;'>En téléchargeant un fichier ou en remplissant les champs demandés.</h6>", unsafe_allow_html=True)

    Fichier = st.toggle('Télécharger un fichier')

    if Fichier : 

        liste_features = ['Pregnancies', 'Glucose', 'BloodPressure', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
        uploaded_file = st.file_uploader("Choisissez un fichier au format .csv : ")
        if uploaded_file is not None:
            try : 
                dataframe = pd.read_csv(uploaded_file)
                try : 
                    df = dataframe[liste_features]
                    st.write('Vérifiez les données chargées : ')
                    st.write(df)
                    if st.button('Soumettre', key = 'soumettre_auto'):
                        #Scalage des données et prédictions :
                        scaler_diabete = load("data_scaler_diabete.skops", trusted=True)
                        algo_diabete = load("data_algo_diabete.skops", trusted=True)
                        scalage_auto = scaler_diabete.transform(df)
                        results_auto = algo_diabete.predict(scalage_auto)
                        
                        st.markdown("<h1 style='text-align: center; color: #227DA7;'>Résultats de l'analyse</h1>", unsafe_allow_html=True)
                        if len(results_auto) == 1 : 
                            for final in results_auto:
                                if final == 1:
                                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Selon vos données renseignées, notre analyse indique que le patient présente un risque élevé de diabète.</h6>", unsafe_allow_html=True)
                                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Cette analyse ne se substitue pas à un avis médical.</h6>", unsafe_allow_html=True)
                                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Si vous n'êtes pas médecin, Nous vous conseillons de vous rapprocher de votre spécialiste</h6>", unsafe_allow_html=True)
                                else:
                                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Selon vos données renseignées, notre analyse indique que le patient présente un faible risque de diabète.</h6>", unsafe_allow_html=True)
                                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Cette analyse ne se substitue pas à un avis médical.</h6>", unsafe_allow_html=True)
                                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Si vous n'êtes pas médecin, Nous vous conseillons de vous rapprocher de votre spécialiste</h6>", unsafe_allow_html=True)
                        else : 
                            df.insert(0, 'Résultats', results_auto)
                            df['Résultats'] = df['Résultats'].replace(0, 'Risque faible').replace(1, 'Risque élevé')
                            st.write(df)
                            st.markdown("<h6 style='text-align: left; color: #012D47;'>Cette analyse ne se substitue pas à un avis médical.</h6>", unsafe_allow_html=True)
                            st.markdown("<h6 style='text-align: left; color: #012D47;'>Si vous n'êtes pas médecin, Nous vous conseillons de vous rapprocher de votre spécialiste</h6>", unsafe_allow_html=True)
                except : 
                    st.write('Les données contenues dans le fichiers ne sont pas reconnues, merci de renseigner les champs ci-dessous : ')
            except : 
                st.write("Un problème a été rencontré lors du téléchargement du fichier ou le fichier n'est pas un CSV.")
                st.write("Veuillez réessayer ou remplissez les champs ci-dessous :")

    Manu = st.toggle('Renseigner les champs')

    if Manu : 

        #Entrée des données patient :
        Age = st.number_input("Entrer l'âge du patient (age) : ", value=None, placeholder="50") # 1
        Pregnancies = st.number_input("Entrer le nombre de grossesses (pregnancies) : ", value=None, placeholder="6")  # 2
        Glucose = st.number_input("Entrer le taux de glucose du patient (mg/dL) (glucose) : ", value=None, placeholder="148") # 3
        BloodPressure = st.number_input("Entrer la pression artérielle (diastolique) du patient (bloodpressure)", value=None, placeholder="72") # 4
        #SkinThickness = st.number_input("Entrer l'épaisseur du pli cutané du triceps du patient (mm) (skintickness) : ")# 5
        Insulin = st.number_input("Entrer le taux d'insuline du patient (mU U/mL)(insulin) : ", value=None, placeholder="169,5") # 6
        BMI = st.number_input("Entrer l'indice de masse corporelle du patient (BMI) : ", value=None, placeholder="33,6") # 7
        DiabetesPedigreeFunction = st.number_input("Entrer les antécédents familliaux du patient (diabetespedigreefunction) : ", value=None, placeholder="0,627") # 8
        
        #Prédictions : 
        if st.button('Soumettre', key = 'soumettre_manu'):
            scaler_diabete = load("data_scaler_diabete.skops", trusted=True)
            algo_diabete = load("data_algo_diabete.skops", trusted=True)
            scalage = scaler_diabete.transform([[Pregnancies, Glucose, BloodPressure, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            results = algo_diabete.predict(scalage)
            
            st.markdown("<h1 style='text-align: center; color: #227DA7;'>Résultats de l'analyse</h1>", unsafe_allow_html=True)
            for final in results:
                if final == 1:
                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Selon vos données renseignées, notre analyse indique que le patient présente un risque élevé de diabète.</h6>", unsafe_allow_html=True)
                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Cette analyse ne se substitue pas à un avis médical.</h6>", unsafe_allow_html=True)
                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Si vous n'êtes pas médecin, Nous vous conseillons de vous rapprocher de votre spécialiste</h6>", unsafe_allow_html=True)
                else:
                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Selon vos données renseignées, notre analyse indique que le patient présente un faible risque de diabète.</h6>", unsafe_allow_html=True)
                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Cette analyse ne se substitue pas à un avis médical.</h6>", unsafe_allow_html=True)
                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Si vous n'êtes pas médecin, Nous vous conseillons de vous rapprocher de votre spécialiste</h6>", unsafe_allow_html=True)

    Specialistes = st.toggle('Je souhaite trouver un spécialiste')

    if Specialistes : 

        #Chargement du dataframe des spécialiste : 
        data_spe = pd.read_csv('data_med.csv', sep=',')
        data_spe['Coordonnées'] = data_spe['Coordonnées'].apply(lambda x: list(map(float, x.split(','))))

        #Filtre du dataframe que pour la maladie : 
        data_diabete = data_spe[data_spe['Profession'] == 'Endocrinologue-diabétologue']

        #Choisir la région : 
        region = [""] + list(data_diabete["Nom Officiel Région"].unique())
        region_user = st.selectbox("Sélectionnez une région",region)

        #Filtre du dataframe sur la région choisie : 
        df_region = data_diabete[data_diabete['Nom Officiel Région'] == region_user].reset_index(drop=True)

        #Création de la carte avec les spécialistes : 
        if region_user != '' : 

            m = folium.Map(location=df_region['Coordonnées'][0], zoom_start=8)
            for index, row in df_region.iterrows():
                folium.Marker(location=row['Coordonnées'], popup=row[['Nom du professionnel','Adresse','Numéro de téléphone']]).add_to(m)
            st_map = st_folium(m, width=700,height=450)
            
        else : 
            st.write('Veuillez sélectionner une région')

def onglet3():  
    
    st.markdown("<h1 style='text-align: center; color: #227DA7;'>Maladie cardiaques</h1>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: left; color: #012D47;'>Entrer les résultats d'analyses du patient</h6>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: left; color: #012D47;'>En téléchargeant un fichier ou en remplissant les champs demandés.</h6>", unsafe_allow_html=True)

    Fichier = st.toggle('Télécharger un fichier')

    if Fichier : 

        liste_features = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
        uploaded_file = st.file_uploader("Choisissez un fichier au format .csv : ")
        if uploaded_file is not None:
            try : 
                dataframe = pd.read_csv(uploaded_file)
                try : 
                    df = dataframe[liste_features]
                    st.write('Vérifiez les données chargées : ')
                    st.write(df)
                    if st.button('Soumettre', key = 'soumettre_auto'):
                        #Scalage des données et prédictions :
                        scaler_cardiaque = load("data_scaler_mal_card.skops", trusted=True)
                        algo_cardiaque = load("data_algo_mal_card.skops", trusted=True)
                        scalage_auto = scaler_cardiaque.transform(df)
                        results_auto = algo_cardiaque.predict(scalage_auto)
                            
                        st.markdown("<h1 style='text-align: center; color: #227DA7;'>Résultats de l'analyse</h1>", unsafe_allow_html=True)
                        if len(results_auto) == 1 : 
                            for final in results_auto:
                                if final == 1:
                                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Selon vos données renseignées, notre analyse indique que le patient présente un risque élevé de maladie cardiaque.</h6>", unsafe_allow_html=True)
                                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Cette analyse ne se substitue pas à un avis médical.</h6>", unsafe_allow_html=True)
                                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Si vous n'êtes pas médecin, Nous vous conseillons de vous rapprocher de votre spécialiste</h6>", unsafe_allow_html=True)
                                else:
                                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Selon vos données renseignées, notre analyse indique que le patient présente un faible risque de maladie cardiaque.</h6>", unsafe_allow_html=True)
                                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Cette analyse ne se substitue pas à un avis médical.</h6>", unsafe_allow_html=True)
                                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Si vous n'êtes pas médecin, Nous vous conseillons de vous rapprocher de votre spécialiste</h6>", unsafe_allow_html=True)
                        else : 
                            df.insert(0, 'Résultats', results_auto)
                            df['Résultats'] = df['Résultats'].replace(0, 'Risque faible').replace(1, 'Risque élevé')
                            st.write(df)
                            st.markdown("<h6 style='text-align: left; color: #012D47;'>Cette analyse ne se substitue pas à un avis médical.</h6>", unsafe_allow_html=True)
                            st.markdown("<h6 style='text-align: left; color: #012D47;'>Si vous n'êtes pas médecin, Nous vous conseillons de vous rapprocher de votre spécialiste</h6>", unsafe_allow_html=True)
                except : 
                    st.write('Les données contenues dans le fichiers ne sont pas reconnues, merci de renseigner les champs ci-dessous : ')
            except : 
                st.write("Un problème a été rencontré lors du téléchargement du fichier ou le fichier n'est pas un CSV.")
                st.write("Veuillez réessayer ou remplissez les champs ci-dessous :")

    Manu = st.toggle('Renseigner les champs')

    if Manu : 

        #Entrée des données patient :
        age = st.number_input("Entrer l'âge du patient (age) : ", value=None, placeholder="583")  # 1
        sex = st.selectbox("Entrer le sexe de patient (1 pour Femme ou 0 pour Homme) (sex) : ", (0,1)) # 2 
        cp = st.selectbox("Entrer le niveau de douleur thoracique du patient (0 à 3) (cp)", (0,1,2,3)) # 3
        trestbps = st.number_input("Entrer la pression artielle (systolique) au repos du patient (trestbps) : ", value=None, placeholder="114")# 4
        chol = st.number_input("Entrer le taux de cholestérol du patient (mg/dL) (chol) : ", value=None, placeholder="318") # 5
        fbs = st.selectbox("Entrer la glycémie à jeûn du patient (0 pour basse et 1 pour élevée) (fbs) : ", (0,1)) # 6
        restecg = st.selectbox("Entrer le résultats électrocardiographiques au repos du patient (0 pour basse et 1 pour élevée) (restecg) : ", (0,1)) # 7
        thalach = st.number_input("Entrer la fréquence cardiaque maximale atteinte du patient (thalach) : ", value=None, placeholder="140")# 8
        exang = st.selectbox("Entrer la présence d'angine provoquée par l'exercice (0 pour absence et 1 pour présence) (exang) : ", (0,1))# 9
        oldpeak = st.number_input("Entrer la dépression du segment ST induite par l'exercice par rapport au repos du patient (oldpeak) : ", value=None, placeholder="4,4")# 10
        slope = st.selectbox("Entrer la pente du segment ST lors de l'exercice du patient (0 à 2) (slope) : ", (0,1,2))# 11
        ca = st.selectbox("Entrer le nombre de vaisseaux sanguins colorés par la fluoroscopie du patient (0 à 4) (ca) : ", (0,1,2,3,4))# 12
        thal = st.selectbox("Entrer le type de thalassémie du patient (thal) (0 à 3) : ", (0,1,2,3))# 13
        
        #Prédictions : 
        if st.button('Soumettre', key = 'soumettre_manu'):
            scaler_cardiaque = load("data_scaler_mal_card.skops", trusted=True)
            algo_cardiaque = load("data_algo_mal_card.skops", trusted=True)
            scalage = scaler_cardiaque.transform([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
            results = algo_cardiaque.predict(scalage)
            
            st.markdown("<h1 style='text-align: center; color: #227DA7;'>Résultats de l'analyse</h1>", unsafe_allow_html=True)
            for final in results:
                if final == 1:
                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Selon vos données renseignées, notre analyse indique que le patient présente un risque élevé de maladie cardiaque.</h6>", unsafe_allow_html=True)
                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Cette analyse ne se substitue pas à un avis médical.</h6>", unsafe_allow_html=True)
                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Si vous n'êtes pas médecin, Nous vous conseillons de vous rapprocher de votre spécialiste</h6>", unsafe_allow_html=True)
                else:
                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Selon vos données renseignées, notre analyse indique que le patient présente un faible risque de maladie cardiaque.</h6>", unsafe_allow_html=True)
                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Cette analyse ne se substitue pas à un avis médical.</h6>", unsafe_allow_html=True)
                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Si vous n'êtes pas médecin, Nous vous conseillons de vous rapprocher de votre spécialiste</h6>", unsafe_allow_html=True)

    Specialistes = st.toggle('Je souhaite trouver un spécialiste')

    if Specialistes : 

        #Chargement du dataframe des spécialiste : 
        data_spe = pd.read_csv('data_med.csv', sep=',')
        data_spe['Coordonnées'] = data_spe['Coordonnées'].apply(lambda x: list(map(float, x.split(','))))

        #Filtre du dataframe que pour la maladie : 
        data_card = data_spe[data_spe['Profession'] == 'Cardiologue']

        #Choisir la région : 
        region = [""] + list(data_card["Nom Officiel Région"].unique())
        region_user = st.selectbox("Sélectionnez une région",region)

        #Filtre du dataframe sur la région choisie : 
        df_region = data_card[data_card['Nom Officiel Région'] == region_user].reset_index(drop=True)

        #Création de la carte avec les spécialistes : 
        if region_user != '' : 

            m = folium.Map(location=df_region['Coordonnées'][0], zoom_start=8)
            for index, row in df_region.iterrows():
                folium.Marker(location=row['Coordonnées'], popup=row[['Nom du professionnel','Adresse','Numéro de téléphone']]).add_to(m)
            st_map = st_folium(m, width=700,height=450)
            
        else : 
            st.write('Veuillez sélectionner une région')

def onglet4():
    
    st.markdown("<h1 style='text-align: center; color: #227DA7;'>Maladie rénale</h1>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: left; color: #012D47;'>Entrer les résultats d'analyses du patient</h6>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: left; color: #012D47;'>En téléchargeant un fichier ou en remplissant les champs demandés.</h6>", unsafe_allow_html=True)

    Fichier = st.toggle('Télécharger un fichier')

    if Fichier : 

        liste_features = ['age', 'al', 'sc', 'htn', 'dm', 'cad']
        uploaded_file = st.file_uploader("Choisissez un fichier au format .csv : ")
        if uploaded_file is not None:
            try : 
                dataframe = pd.read_csv(uploaded_file)
                try : 
                    df = dataframe[liste_features]
                    st.write('Vérifiez les données chargées : ')
                    st.write(df)
                    if st.button('Soumettre', key = 'soumettre_auto'):
                        #Scalage des données et prédictions :
                        scaler_rein = load("data_scaler_reins.skops", trusted=True)
                        algo_rein = load("data_algo_reins.skops", trusted=True)
                        scalage_auto = scaler_rein.transform(df)
                        results_auto = algo_rein.predict(scalage_auto)
                            
                        st.markdown("<h1 style='text-align: center; color: #227DA7;'>Résultats de l'analyse</h1>", unsafe_allow_html=True)
                        if len(results_auto) == 1 : 
                            for final in results_auto:
                                if final == 1:
                                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Selon vos données renseignées, notre analyse indique que le patient présente un risque élevé de maladie rénale.</h6>", unsafe_allow_html=True)
                                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Cette analyse ne se substitue pas à un avis médical.</h6>", unsafe_allow_html=True)
                                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Si vous n'êtes pas médecin, Nous vous conseillons de vous rapprocher de votre spécialiste</h6>", unsafe_allow_html=True)
                                else:
                                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Selon vos données renseignées, notre analyse indique que le patient présente un faible risque de maladie rénale.</h6>", unsafe_allow_html=True)
                                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Cette analyse ne se substitue pas à un avis médical.</h6>", unsafe_allow_html=True)
                                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Si vous n'êtes pas médecin, Nous vous conseillons de vous rapprocher de votre spécialiste</h6>", unsafe_allow_html=True)
                        else : 
                            df.insert(0, 'Résultats', results_auto)
                            df['Résultats'] = df['Résultats'].replace(0, 'Risque faible').replace(1, 'Risque élevé')
                            st.write(df)
                            st.markdown("<h6 style='text-align: left; color: #012D47;'>Cette analyse ne se substitue pas à un avis médical.</h6>", unsafe_allow_html=True)
                            st.markdown("<h6 style='text-align: left; color: #012D47;'>Si vous n'êtes pas médecin, Nous vous conseillons de vous rapprocher de votre spécialiste</h6>", unsafe_allow_html=True)
                except : 
                    st.write('Les données contenues dans le fichiers ne sont pas reconnues, merci de renseigner les champs ci-dessous : ')
            except : 
                st.write("Un problème a été rencontré lors du téléchargement du fichier ou le fichier n'est pas un CSV.")
                st.write("Veuillez réessayer ou remplissez les champs ci-dessous :")

    Manu = st.toggle('Renseigner les champs')

    if Manu : 

        #Entrée des données patient :
        age = st.number_input("Entrer l'âge du patient (age) :", value=None, placeholder="25")  # 1
        #bp = st.number_input("Entrer la pression artérielle diastolique du patient (bp) :") # 2 
        #sg = st.number_input("Entrer la gravité spécifique (densité) de l'urine du patient (sg) :") # 3
        al = st.selectbox("Entrer le niveau d'albumine dans le sang du patient (0 à 5) (al) :", (0,1,2,3,4,5))# 4
        #su = st.number_input("Entrer le niveau de sucre dans le sang du patient (su) :") # 5
        #rbc = st.number_input("Entrer la concentration de globules rouge dans le sang du patient (rbc) : ") # 6
        #pc = st.number_input("Entrer la présence de cellules de pus (0 = absence, 1 = présence) chez le patient (pc): ") # 7
        #pcc = st.number_input("Entrer la présence d'aggrégats de cellules de pus dans l'urine (0 = absence, 1 = présence) chez le patient (pcc) :")# 8
        #ba = st.number_input("Entrer la présence de bactérie dans l'urine (0 = absence, 1 = présence) du patient (ba) :")# 9
        #bgr = st.number_input("Entrer le taux sanguin aléatoire de glucose (mg/dL) du patient (bgr) :")# 10
        #bu = st.number_input("Entrer la concentration d'urée sanguine (mmol/L) du patient (bu) :")# 11
        sc = st.number_input("Entrer le taux de créatinine sérique (mL/min) du patient (sc) :", value=None, placeholder="6,7")# 12
        #sod = st.number_input("Entrer le taux de sodium dans le sang (mEg/L) du patient (sod) :")# 13
        #pot = st.number_input("Entrer le taux de potasium dans le sang (mmol/L) du patient (pot) :")# 14
        #hemo = st.number_input("Entrer le taux d'hémoglobine dans le sang (g/dL) du patient (hemo) :")# 15
        #pcv = st.number_input("Entrer le volume de globule rouge tassé du patient (pcv) :")# 16
        #wc = st.number_input("Entrer le volume de leucocytes (mL) du patient (wc) :")# 17
        #rc = st.number_input("Entrer le nombre de globules rouge ???? du patient (rc) :")# 18
        htn = st.selectbox("Entrer la présence d'hypertension (0 = absence, 1 = présence) chez le patient (htn) :", (0,1))# 19
        dm = st.selectbox("Entrer la présence de diabète (0 = absence, 1 = présence) chez le patient (dm) :", (0,1))# 20
        cad = st.selectbox("Entrer la présence de maladies coronariennes (0 = absence, 1 = présence) chez le patient (cad) :", (0,1))# 21
        #appet =  st.number_input("Entrer le niveau d'appétit (0 = absence, 1 = présence) du patient (appet) :")# 22
        #pe =  st.number_input("Entrer la présence d'oedème périphérique (pieds, chevilles, jambes, mains) (0 = absence, 1 = présence) chez le patient :")# 23
        #ane =  st.number_input("Entrer la présence d'anémie (0 = absence, 1 = présence) chez le patient :")# 24
        
        #Prédictions : 
        if st.button('Soumettre', key = 'soumettre_manu'):
            scaler_rein = load("data_scaler_reins.skops", trusted=True)
            algo_rein = load("data_algo_reins.skops", trusted=True)
            scalage = scaler_rein.transform([[age, al, sc, htn, dm, cad]])
            results = algo_rein.predict(scalage)
            
            st.markdown("<h1 style='text-align: center; color: #227DA7;'>Résultats de l'analyse</h1>", unsafe_allow_html=True)
            for final in results:
                if final == 1:
                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Selon vos données renseignées, notre analyse indique que le patient présente un risque élevé de maladie rénale.</h6>", unsafe_allow_html=True)
                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Cette analyse ne se substitue pas à un avis médical.</h6>", unsafe_allow_html=True)
                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Si vous n'êtes pas médecin, Nous vous conseillons de vous rapprocher de votre spécialiste</h6>", unsafe_allow_html=True)
                else:
                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Selon vos données renseignées, notre analyse indique que le patient présente un faible risque de maladie rénale.</h6>", unsafe_allow_html=True)
                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Cette analyse ne se substitue pas à un avis médical.</h6>", unsafe_allow_html=True)
                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Si vous n'êtes pas médecin, Nous vous conseillons de vous rapprocher de votre spécialiste</h6>", unsafe_allow_html=True)

    Specialistes = st.toggle('Je souhaite trouver un spécialiste')

    if Specialistes : 

        #Chargement du dataframe des spécialiste : 
        data_spe = pd.read_csv('data_med.csv', sep=',')
        data_spe['Coordonnées'] = data_spe['Coordonnées'].apply(lambda x: list(map(float, x.split(','))))

        #Filtre du dataframe que pour la maladie : 
        data_rein = data_spe[data_spe['Profession'] == 'Néphrologue']

        #Choisir la région : 
        region = [""] + list(data_rein["Nom Officiel Région"].unique())
        region_user = st.selectbox("Sélectionnez une région",region)

        #Filtre du dataframe sur la région choisie : 
        df_region = data_rein[data_rein['Nom Officiel Région'] == region_user].reset_index(drop=True)

        #Création de la carte avec les spécialistes : 
        if region_user != '' : 

            m = folium.Map(location=df_region['Coordonnées'][0], zoom_start=8)
            for index, row in df_region.iterrows():
                folium.Marker(location=row['Coordonnées'], popup=row[['Nom du professionnel','Adresse','Numéro de téléphone']]).add_to(m)
            st_map = st_folium(m, width=700,height=450)
            
        else : 
            st.write('Veuillez sélectionner une région')

def onglet5():

    st.markdown("<h1 style='text-align: center; color: #227DA7;'>Maladie du foie</h1>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: left; color: #012D47;'>Entrer les résultats d'analyses du patient</h6>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: left; color: #012D47;'>En téléchargeant un fichier ou en remplissant les champs demandés.</h6>", unsafe_allow_html=True)
    Fichier = st.toggle('Télécharger un fichier')

    if Fichier : 

        liste_features = ['Age', 'Total_Bilirubin', 'Alkaline_Phosphotase', 'Alamine_Aminotransferase', 'Albumin_and_Globulin_Ratio', 'gender_fact']
        uploaded_file = st.file_uploader("Choisissez un fichier au format .csv : ")
        if uploaded_file is not None:
            try : 
                dataframe = pd.read_csv(uploaded_file)
                try : 
                    df = dataframe[liste_features]
                    st.write('Vérifiez les données chargées : ')
                    st.write(df)
                    if st.button('Soumettre', key = 'soumettre_auto'):
                        #Scalage des données et prédictions :
                        scaler_foie = load("data_scaler_Foie.skops", trusted=True)
                        algo_foie = load("data_algo_Foie.skops", trusted=True)
                        scalage_auto = scaler_foie.transform(df)
                        results_auto = algo_foie.predict(scalage_auto)
                            
                        st.markdown("<h1 style='text-align: center; color: #227DA7;'>Résultats de l'analyse</h1>", unsafe_allow_html=True)
                        if len(results_auto) == 1 : 
                            for final in results_auto:
                                if final == 1:
                                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Selon vos données renseignées, notre analyse indique que le patient présente un risque élevé de maladie du foie.</h6>", unsafe_allow_html=True)
                                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Cette analyse ne se substitue pas à un avis médical.</h6>", unsafe_allow_html=True)
                                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Si vous n'êtes pas médecin, Nous vous conseillons de vous rapprocher de votre spécialiste</h6>", unsafe_allow_html=True)
                                else:
                                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Selon vos données renseignées, notre analyse indique que le patient présente un faible risque de maladie du foie.</h6>", unsafe_allow_html=True)
                                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Cette analyse ne se substitue pas à un avis médical.</h6>", unsafe_allow_html=True)
                                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Si vous n'êtes pas médecin, Nous vous conseillons de vous rapprocher de votre spécialiste</h6>", unsafe_allow_html=True)
                        else : 
                            df.insert(0, 'Résultats', results_auto)
                            df['Résultats'] = df['Résultats'].replace(0, 'Risque faible').replace(1, 'Risque élevé')
                            st.write(df)
                            st.markdown("<h6 style='text-align: left; color: #012D47;'>Cette analyse ne se substitue pas à un avis médical.</h6>", unsafe_allow_html=True)
                            st.markdown("<h6 style='text-align: left; color: #012D47;'>Si vous n'êtes pas médecin, Nous vous conseillons de vous rapprocher de votre spécialiste</h6>", unsafe_allow_html=True)
                except : 
                    st.write('Les données contenues dans le fichiers ne sont pas reconnues, merci de renseigner les champs ci-dessous : ')
            except : 
                st.write("Un problème a été rencontré lors du téléchargement du fichier ou le fichier n'est pas un CSV.")
                st.write("Veuillez réessayer ou remplissez les champs ci-dessous :")

    Manu = st.toggle('Renseigner les champs')

    if Manu : 

        #Entrée des données patient :
        Age = st.number_input("Entrez l'âge du patient (age) :", value=None, placeholder="65")  # 1
        gender_fact = st.selectbox("Entrez le genre (0 pour Femme ou 1 pour Homme) du patient (gender_fact): ", (0,1)) # 2
        Total_Bilirubin = st.number_input("Entrez la valeur de la Bilirubine totale du patient (mg/dL) (total_bilirubin) :", value=None, placeholder="0,7") # 3 
        Alkaline_Phosphotase = st.number_input("Entrez la valeur de la Phosphatase alcaline - Enzyme (PAL) du patient (UI/L) (alkaline_phosphatase) :", value=None, placeholder="187") # 4
        Alamine_Aminotransferase = st.number_input("Entrez la valeur de l'Alanine aminotransférase (ALAT) du patient (transaminase) (UI/L) (alamine_aminnotransferase) :", value=None, placeholder="16")# 5
        Albumin_and_Globulin_Ratio = st.number_input("Entrez la valeur du Rapport albumine/globuline du patient (albumin_and_globulin_ratio):", value=None, placeholder="0,9") # 6

        #Prédictions : 
        if st.button('Soumettre', key='soumettre_manu'):
            scaler_foie = load("data_scaler_Foie.skops", trusted=True)
            algo_foie = load("data_algo_Foie.skops", trusted=True)
            scalage = scaler_foie.transform([[Age, Total_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase, Albumin_and_Globulin_Ratio, gender_fact]])
            results = algo_foie.predict(scalage)
            
            st.markdown("<h1 style='text-align: center; color: #227DA7;'>Résultats de l'analyse</h1>", unsafe_allow_html=True)
            for final in results:
                if final == 1:
                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Selon vos données renseignées, notre analyse indique que le patient présente un risque élevé de maladie du foie.</h6>", unsafe_allow_html=True)
                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Cette analyse ne se substitue pas à un avis médical.</h6>", unsafe_allow_html=True)
                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Si vous n'êtes pas médecin, Nous vous conseillons de vous rapprocher de votre spécialiste</h6>", unsafe_allow_html=True)
                else:
                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Selon vos données renseignées, notre analyse indique que le patient présente un faible risque de maladie du foie.</h6>", unsafe_allow_html=True)
                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Cette analyse ne se substitue pas à un avis médical.</h6>", unsafe_allow_html=True)
                    st.markdown("<h6 style='text-align: left; color: #012D47;'>Si vous n'êtes pas médecin, Nous vous conseillons de vous rapprocher de votre spécialiste</h6>", unsafe_allow_html=True)

    Specialistes = st.toggle('Je souhaite trouver un spécialiste')

    if Specialistes : 

        #Chargement du dataframe des spécialiste : 
        data_spe = pd.read_csv('data_med.csv', sep=',')
        data_spe['Coordonnées'] = data_spe['Coordonnées'].apply(lambda x: list(map(float, x.split(','))))

        #Filtre du dataframe que pour la maladie : 
        data_foie = data_spe[data_spe['Profession'] == 'Gastro-entérologue et hépatologue']

        #Choisir la région : 
        region = [""] + list(data_foie["Nom Officiel Région"].unique())
        region_user = st.selectbox("Sélectionnez une région",region)

        #Filtre du dataframe sur la région choisie : 
        df_region = data_foie[data_foie['Nom Officiel Région'] == region_user].reset_index(drop=True)

        #Création de la carte avec les spécialistes : 
        if region_user != '' : 

            m = folium.Map(location=df_region['Coordonnées'][0], zoom_start=8)
            for index, row in df_region.iterrows():
                folium.Marker(location=row['Coordonnées'], popup=row[['Nom du professionnel','Adresse','Numéro de téléphone']]).add_to(m)
            st_map = st_folium(m, width=700,height=450)
            
        else : 
            st.write('Veuillez sélectionner une région')

def main():
    st.sidebar.image('data_analytics.png')
    st.sidebar.title("Navigation")
    onglet_selectionne = st.sidebar.selectbox("Sélectionner un onglet", ["Accueil", "Cancer du sein", "Diabète", "Maladie cardiaque", "Maladie rénale", "Maladie du foie"])

    if onglet_selectionne == "Accueil":
        onglet0()
    elif onglet_selectionne == "Cancer du sein":
        onglet1()
    elif onglet_selectionne == "Diabète":
        onglet2()
    elif onglet_selectionne == "Maladie cardiaque":
        onglet3()
    elif onglet_selectionne == "Maladie rénale" :
        onglet4()
    elif onglet_selectionne == "Maladie du foie" :
        onglet5()

if __name__ == "__main__":
    main()
