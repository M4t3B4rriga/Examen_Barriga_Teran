# Proyecto de Aprendizaje Automático Barriga-Teran 

## Instalación 
1. Clona este repositorio:
    ```sh
    git clone https://github.com/M4t3B4rriga/Examen_Barriga_Teran
    ```
2. Entreamos a Anaconda Prompt y entramos al directorio de la carpeta donde esta el programa:
    ```sh
    cd \Desktop\API_Gcloud_Streamlit-master\API_Gcloud_Streamlit-master
    ```
3. Ya entrando a esa ruta toca ir instalando las dependencias faltantes
    ```sh
    pip install --upgrade protobuf
    ```
   ```sh
    pip install streamlit
   ```
   ```sh
    pip install protobuf==3.20.x
   ```

4. Ya teniendo actualizando verificamos que todo este actualizado

 ```sh
   pip install --upgrade flask
   ```
 ```sh
   pip install --upgrade jinja2
   ```
5.  Instalado lo necesario se procede a crear un Apicrop
 ```sh
   conda create -n ApiCrop
   ```
6. Se activa el Apicrop
    ```sh
   activate ApiCrop
   ```
7. Una vez hecho la activacion de Apicrop se necesita instalar python
  ```sh
    conda install python=3.7
   ```
8. Las ultimas instalaciones seria lo que se tiene en "requirements.txt"
 ```sh
     pip install -r requirements.txt
   ```
9. Ya teniendo todo , se puede iniciar el programa
     ```sh
   streamlit run app.py
      ```
