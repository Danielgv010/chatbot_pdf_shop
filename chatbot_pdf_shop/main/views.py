import logging
import json
from django.shortcuts import render
from .document import Document

from django.http import JsonResponse
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

import os
from chatbot_pdf_shop.settings import BASE_DIR
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from azure.storage.blob import ContainerClient
from azure.ai.language.conversations import ConversationAnalysisClient


load_dotenv(os.path.join(BASE_DIR, "main", ".env"))

AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
CONTAINER_NAME = os.getenv("BLOB_CONTAINER_NAME")
UPLOADS_CONTAINER_NAME = os.getenv("BLOB_UPLOADS_CONTAINER_NAME")

data = []

def analyze_layout_all(request):
    endpoint = os.getenv("AZURE_OCR_ENDPOINT")
    key = os.getenv("AZURE_OCR_KEY")
    model_id = "pc_shop_chatbot"

    document_intelligence_client  = DocumentIntelligenceClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )

    container_client = ContainerClient.from_connection_string(
        AZURE_STORAGE_CONNECTION_STRING, CONTAINER_NAME
    )

    blob_list = container_client.list_blobs()

    for blob in blob_list:
        if blob.name.lower().endswith(".pdf"):
            form_url = f"https://{container_client.account_name}.blob.core.windows.net/{CONTAINER_NAME}/{blob.name}"
            
            try:
                poller = document_intelligence_client.begin_analyze_document(
                    model_id, AnalyzeDocumentRequest(url_source=form_url)
                )
                result = poller.result()
                
                for idx, document in enumerate(result.documents):
                    document_object = Document(
                        empresa=document.fields.get("Empresa", {}).get("valueString"),
                        direccion_empresa=document.fields.get("DireccionEmpresa", {}).get("valueString"),
                        producto=document.fields.get("Producto", {}).get("valueString"),
                        codigo_producto=document.fields.get("CodigoProducto", {}).get("valueString"),
                        precio=document.fields.get("Precio", {}).get("valueString"),
                        garantia=document.fields.get("Garantia", {}).get("valueString"),
                        disco_disco=document.fields.get("Disco", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("Disco", {}).get("valueString"),
                        disco_capacidad=document.fields.get("Disco", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("Capacidad", {}).get("valueString"),
                        disco_tipo_soporte=document.fields.get("Disco", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("TipoSoporte1", {}).get("valueString"),
                        disco_interfaz_soporte=document.fields.get("Disco", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("InterfazSoporte1", {}).get("valueString"),
                        disco_velocidad_soporte=document.fields.get("Disco", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("VelocidadSoporte1", {}).get("valueString"),
                        disco_numero_soportes=document.fields.get("Disco", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("NúmeroSoportes", {}).get("valueString"),
                        gpu_integrada=document.fields.get("Gpu", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("GraficaIntegrada", {}).get("valueString"),
                        gpu_fabricante=document.fields.get("Gpu", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("FabricanteGpu", {}).get("valueString"),
                        gpu_modelo=document.fields.get("Gpu", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("ModeloGpu", {}).get("valueString"),
                        gpu_memoria=document.fields.get("Gpu", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("MemoriaGpu", {}).get("valueString"),
                        cpu_familia=document.fields.get("Cpu", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("FamiliaCpu", {}).get("valueString"),
                        cpu_modelo=document.fields.get("Cpu", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("ModeloCpu", {}).get("valueString"),
                        cpu_fabricante=document.fields.get("Cpu", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("FabricanteCpu", {}).get("valueString"),
                        cpu_generacion=document.fields.get("Cpu", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("GeneracionProcesador", {}).get("valueString"),
                        cpu_nucleos=document.fields.get("Cpu", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("NucleosCpu", {}).get("valueNumber"),
                        cpu_frecuencia=document.fields.get("Cpu", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("FrecuenciaCpu", {}).get("valueString"),
                        cpu_frecuencia_turbo=document.fields.get("Cpu", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("FrecuenciaTurboCpu", {}).get("valueString"),
                        pantalla_size=document.fields.get("Pantalla", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("TamanoPantalla", {}).get("valueString"),
                        pantalla_tactil=document.fields.get("Pantalla", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("PantallaTactil", {}).get("valueString"),
                        pantalla_tipo=document.fields.get("Pantalla", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("TipoPantalla", {}).get("valueString"),
                        pantalla_resolucion=document.fields.get("Pantalla", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("ResolucionPantalla", {}).get("valueString"),
                        pantalla_luminosidad=document.fields.get("Pantalla", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("Luminosidad", {}).get("valueString"),
                        pantalla_contraste=document.fields.get("Pantalla", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("Contraste", {}).get("valueString"),
                        pantalla_tipologia_hd=document.fields.get("Pantalla", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("TipologiaHd", {}).get("valueString"),
                        pantalla_retroiluminacion=document.fields.get("Pantalla", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("Retroiluminacion", {}).get("valueString"),
                        pantalla_relacion_aspecto=document.fields.get("Pantalla", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("RelacionAspecto", {}).get("valueString"),
                        pantalla_tiempo_maximo_refresco=document.fields.get("Pantalla", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("TiempoMaximoDeRefresco", {}).get("valueString"),
                        pantalla_espacio_rgb=document.fields.get("Pantalla", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("EspacioRGB", {}).get("valueString"),
                        pantalla_superficie=document.fields.get("Pantalla", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("SuperficiePantalla", {}).get("valueString"),
                        dimensiones_peso=document.fields.get("DimensionesPeso", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("Peso", {}).get("valueString"),
                        dimensiones_altura=document.fields.get("DimensionesPeso", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("Altura", {}).get("valueString"),
                        dimensiones_ancho=document.fields.get("DimensionesPeso", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("Ancho", {}).get("valueString"),
                        dimensiones_profundidad=document.fields.get("DimensionesPeso", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("Profundidad", {}).get("valueString"),
                        general_color=document.fields.get("General", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("Color", {}).get("valueString"),
                        general_tpm=document.fields.get("General", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("TPM", {}).get("valueString"),
                        general_material_chasis=document.fields.get("General", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("MaterialChasis", {}).get("valueString"),
                        general_deteccion_huella=document.fields.get("General", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("DeteccionHuella", {}).get("valueString"),
                        general_potencia_adaptador_ac=document.fields.get("General", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("PotenciaAdaptadorAC", {}).get("valueString"),
                        general_2_en_1_detachable=document.fields.get("General", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("2En1Detachable", {}).get("valueString"),
                        conexiones_red_movil=document.fields.get("Conexiones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("RedMovil", {}).get("valueString"),
                        conexiones_total_usb=document.fields.get("Conexiones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("TotalUSB", {}).get("valueString"),
                        conexiones_usb_2_0=document.fields.get("Conexiones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("USB2.0", {}).get("valueString"),
                        conexiones_usb_3_2=document.fields.get("Conexiones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("USB3.2", {}).get("valueString"),
                        conexiones_ethernet=document.fields.get("Conexiones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("Ethernet", {}).get("valueString"),
                        conexiones_vga=document.fields.get("Conexiones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("VGA", {}).get("valueString"),
                        conexiones_bluetooth=document.fields.get("Conexiones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("Bluetooth", {}).get("valueString"),
                        conexiones_version_bluetooth=document.fields.get("Conexiones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("VersionBluetooth", {}).get("valueString"),
                        conexiones_thunderbolt=document.fields.get("Conexiones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("Thunderbolt", {}).get("valueString"),
                        conexiones_hdmi=document.fields.get("Conexiones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("HDMI", {}).get("valueString"),
                        conexiones_hdmi_micro=document.fields.get("Conexiones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("HDMIMicro", {}).get("valueString"),
                        conexiones_display_port=document.fields.get("Conexiones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("DisplayPort", {}).get("valueString"),
                        conexiones_mini_display_port=document.fields.get("Conexiones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("MiniDisplayPort", {}).get("valueString"),
                        conexiones_dockstation=document.fields.get("Conexiones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("ConextionDockStation", {}).get("valueString"),
                        conexiones_wireless=document.fields.get("Conexiones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("Wireless", {}).get("valueString"),
                        conexiones_puerto_carga=document.fields.get("Conexiones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("PuertoCarga", {}).get("valueString"),
                        conexiones_otras=document.fields.get("Conexiones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("OtrasConexiones", {}).get("valueString"),
                        ram_instalada=document.fields.get("RAM", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("RamInstalada", {}).get("valueString"),
                        ram_maxima=document.fields.get("RAM", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("RamMaxima", {}).get("valueString"),
                        ram_bancos_libres=document.fields.get("RAM", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("BancosRamLibres", {}).get("valueString"),
                        ram_velocidad=document.fields.get("RAM", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("VelocidadRam", {}).get("valueString"),
                        ram_tecnologia=document.fields.get("RAM", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("TecnologiaRam", {}).get("valueString"),
                        ram_tipo=document.fields.get("RAM", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("TipoRam", {}).get("valueString"),
                        tipologia_unidad=document.fields.get("TipologiaUnidad", {}).get("valueString"),
                        teclado_numerico=document.fields.get("Teclado", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("TecladoNumerico", {}).get("valueString"),
                        teclado_numero_teclas=document.fields.get("Teclado", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("NumeroTeclas", {}).get("valueString"),
                        teclado_retroiluminado=document.fields.get("Teclado", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("TecladoRetroiluminado", {}).get("valueString"),
                        audio_microfono_integrado=document.fields.get("Audio", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("MicrofonoIntegrado", {}).get("valueString"),
                        audio_fabricante_altavoces=document.fields.get("Audio", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("FabricanteAltavoces", {}).get("valueString"),
                        bateria_celdas=document.fields.get("Bateria", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("Celdas", {}).get("valueString"),
                        bateria_duracion=document.fields.get("Bateria", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("DuracionBateria", {}).get("valueString"),
                        webcam_integrada=document.fields.get("Webcam", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("WebcamIntegrada", {}).get("Webcam", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("Integrada", {}).get("valueString"),
                        webcam_resolucion=document.fields.get("Webcam", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("ResolucionWebcam", {}).get("valueString"),
                        webcam_infrarrojos=document.fields.get("Webcam", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("Infrarrojos", {}).get("valueString"),
                        webcam_tipo_camara_frontal=document.fields.get("Webcam", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("TipoCamaraFrontal", {}).get("valueString"),
                        lectores_memoria_compact_flash=document.fields.get("LectoresMemory", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("CompactFlash", {}).get("valueString"),
                        lectores_memoria_memory_stick=document.fields.get("LectoresMemory", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("MemoryStick", {}).get("valueString"),
                        lectores_memoria_memory_stick_duo=document.fields.get("LectoresMemory", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("MemoryStickDuo", {}).get("valueString"),
                        lectores_memoria_memory_stick_pro=document.fields.get("LectoresMemory", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("MemoryStickPro", {}).get("valueString"),
                        lectores_memoria_memory_stick_pro_duo=document.fields.get("LectoresMemory", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("MemoryStickProDuo", {}).get("valueString"),
                        lectores_memoria_memory_stick_pro_hg_duo=document.fields.get("LectoresMemory", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("MemoryStickProHG_Duo", {}).get("valueString"),
                        lectores_memoria_memory_stick_micro=document.fields.get("LectoresMemory", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("MemoryStickMicro", {}).get("valueString"),
                        lectores_memoria_micro_sd=document.fields.get("LectoresMemory", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("MicroSD", {}).get("valueString"),
                        lectores_memoria_multimedia_card=document.fields.get("LectoresMemory", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("MultimediaCard", {}).get("valueString"),
                        lectores_memoria_mmc_plus=document.fields.get("LectoresMemory", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("MMCPlus", {}).get("valueString"),
                        lectores_memoria_multimedia_card_reduced_size=document.fields.get("LectoresMemory", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("MultimediaCardReducedSize", {}).get("valueString"),
                        lectores_memoria_secure_digital_card=document.fields.get("LectoresMemory", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("SecureDigitalCard", {}).get("valueString"),
                        lectores_memoria_secure_digital_mini=document.fields.get("LectoresMemory", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("SecureDigitalMini", {}).get("valueString"),
                        sistema_software_version_so=document.fields.get("SistemaYSoftware", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("VersionSO", {}).get("valueString"),
                        sistema_software_bits_so=document.fields.get("SistemaYSoftware", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("BitSO", {}).get("valueString"),
                        sistema_software_software_incluido=document.fields.get("SistemaYSoftware", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("SoftwareIncluido", {}).get("valueString"),
                        soluciones=document.fields.get("Soluciones", {}).get("valueString"),
                        size_embalaje_lado_a=document.fields.get("TamañoEmbalaje", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("LadoA", {}).get("valueString"),
                        size_embalaje_lado_b=document.fields.get("TamañoEmbalaje", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("LadoB", {}).get("valueString"),
                        size_embalaje_lado_c=document.fields.get("TamañoEmbalaje", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("LadoC", {}).get("valueString"),
                        size_embalaje_peso=document.fields.get("TamañoEmbalaje", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("Peso", {}).get("valueString"),
                        certificaciones_energy_star=document.fields.get("Certificaciones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("EnergyStar", {}).get("valueString"),
                        certificaciones_wifi=document.fields.get("Certificaciones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("WiFi", {}).get("valueString"),
                        certificaciones_otras=document.fields.get("Certificaciones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("Otras", {}).get("valueString"),
                        descripcion=document.fields.get("Descripcion", {}).get("valueString")
                    )
                    save(document_object)
            
            except Exception as e:
                logging.error(f"Error processing {blob.name}: {e}")

@csrf_exempt
def analyze_layout(request):
    try:
        if request.method == "POST" and request.FILES.get('file'):
            uploaded_file = request.FILES['file']
            file_name = uploaded_file.name

            container_name = os.getenv("BLOB_UPLOADS_CONTAINER_NAME")
            if not container_name:
                raise ValueError("BLOB_UPLOADS_CONTAINER_NAME is not defined in environment variables.")

            container_client = ContainerClient.from_connection_string(
                os.getenv("AZURE_STORAGE_CONNECTION_STRING"), 
                container_name
            )

            blob_client = container_client.get_blob_client(file_name)
            blob_client.upload_blob(uploaded_file.read(), overwrite=True)

            endpoint = os.getenv("AZURE_OCR_ENDPOINT")
            key = os.getenv("AZURE_OCR_KEY")
            model_id = "pc_shop_chatbot"
            
            document_intelligence_client = DocumentIntelligenceClient(
                endpoint=endpoint, credential=AzureKeyCredential(key)
            )

            form_url = f"https://{container_client.account_name}.blob.core.windows.net/{container_name}/{file_name}"

            poller = document_intelligence_client.begin_analyze_document(
                model_id, AnalyzeDocumentRequest(url_source=form_url)
            )
            result = poller.result()

            for idx, document in enumerate(result.documents):
                document_object = Document(
                        empresa=document.fields.get("Empresa", {}).get("valueString"),
                        direccion_empresa=document.fields.get("DireccionEmpresa", {}).get("valueString"),
                        producto=document.fields.get("Producto", {}).get("valueString"),
                        codigo_producto=document.fields.get("CodigoProducto", {}).get("valueString"),
                        precio=document.fields.get("Precio", {}).get("valueString"),
                        garantia=document.fields.get("Garantia", {}).get("valueString"),
                        disco_disco=document.fields.get("Disco", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("Disco", {}).get("valueString"),
                        disco_capacidad=document.fields.get("Disco", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("Capacidad", {}).get("valueString"),
                        disco_tipo_soporte=document.fields.get("Disco", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("TipoSoporte1", {}).get("valueString"),
                        disco_interfaz_soporte=document.fields.get("Disco", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("InterfazSoporte1", {}).get("valueString"),
                        disco_velocidad_soporte=document.fields.get("Disco", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("VelocidadSoporte1", {}).get("valueString"),
                        disco_numero_soportes=document.fields.get("Disco", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("NúmeroSoportes", {}).get("valueString"),
                        gpu_integrada=document.fields.get("Gpu", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("GraficaIntegrada", {}).get("valueString"),
                        gpu_fabricante=document.fields.get("Gpu", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("FabricanteGpu", {}).get("valueString"),
                        gpu_modelo=document.fields.get("Gpu", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("ModeloGpu", {}).get("valueString"),
                        gpu_memoria=document.fields.get("Gpu", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("MemoriaGpu", {}).get("valueString"),
                        cpu_familia=document.fields.get("Cpu", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("FamiliaCpu", {}).get("valueString"),
                        cpu_modelo=document.fields.get("Cpu", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("ModeloCpu", {}).get("valueString"),
                        cpu_fabricante=document.fields.get("Cpu", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("FabricanteCpu", {}).get("valueString"),
                        cpu_generacion=document.fields.get("Cpu", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("GeneracionProcesador", {}).get("valueString"),
                        cpu_nucleos=document.fields.get("Cpu", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("NucleosCpu", {}).get("valueNumber"),
                        cpu_frecuencia=document.fields.get("Cpu", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("FrecuenciaCpu", {}).get("valueString"),
                        cpu_frecuencia_turbo=document.fields.get("Cpu", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("FrecuenciaTurboCpu", {}).get("valueString"),
                        pantalla_size=document.fields.get("Pantalla", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("TamanoPantalla", {}).get("valueString"),
                        pantalla_tactil=document.fields.get("Pantalla", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("PantallaTactil", {}).get("valueString"),
                        pantalla_tipo=document.fields.get("Pantalla", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("TipoPantalla", {}).get("valueString"),
                        pantalla_resolucion=document.fields.get("Pantalla", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("ResolucionPantalla", {}).get("valueString"),
                        pantalla_luminosidad=document.fields.get("Pantalla", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("Luminosidad", {}).get("valueString"),
                        pantalla_contraste=document.fields.get("Pantalla", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("Contraste", {}).get("valueString"),
                        pantalla_tipologia_hd=document.fields.get("Pantalla", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("TipologiaHd", {}).get("valueString"),
                        pantalla_retroiluminacion=document.fields.get("Pantalla", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("Retroiluminacion", {}).get("valueString"),
                        pantalla_relacion_aspecto=document.fields.get("Pantalla", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("RelacionAspecto", {}).get("valueString"),
                        pantalla_tiempo_maximo_refresco=document.fields.get("Pantalla", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("TiempoMaximoDeRefresco", {}).get("valueString"),
                        pantalla_espacio_rgb=document.fields.get("Pantalla", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("EspacioRGB", {}).get("valueString"),
                        pantalla_superficie=document.fields.get("Pantalla", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("SuperficiePantalla", {}).get("valueString"),
                        dimensiones_peso=document.fields.get("DimensionesPeso", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("Peso", {}).get("valueString"),
                        dimensiones_altura=document.fields.get("DimensionesPeso", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("Altura", {}).get("valueString"),
                        dimensiones_ancho=document.fields.get("DimensionesPeso", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("Ancho", {}).get("valueString"),
                        dimensiones_profundidad=document.fields.get("DimensionesPeso", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("Profundidad", {}).get("valueString"),
                        general_color=document.fields.get("General", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("Color", {}).get("valueString"),
                        general_tpm=document.fields.get("General", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("TPM", {}).get("valueString"),
                        general_material_chasis=document.fields.get("General", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("MaterialChasis", {}).get("valueString"),
                        general_deteccion_huella=document.fields.get("General", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("DeteccionHuella", {}).get("valueString"),
                        general_potencia_adaptador_ac=document.fields.get("General", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("PotenciaAdaptadorAC", {}).get("valueString"),
                        general_2_en_1_detachable=document.fields.get("General", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("2En1Detachable", {}).get("valueString"),
                        conexiones_red_movil=document.fields.get("Conexiones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("RedMovil", {}).get("valueString"),
                        conexiones_total_usb=document.fields.get("Conexiones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("TotalUSB", {}).get("valueString"),
                        conexiones_usb_2_0=document.fields.get("Conexiones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("USB2.0", {}).get("valueString"),
                        conexiones_usb_3_2=document.fields.get("Conexiones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("USB3.2", {}).get("valueString"),
                        conexiones_ethernet=document.fields.get("Conexiones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("Ethernet", {}).get("valueString"),
                        conexiones_vga=document.fields.get("Conexiones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("VGA", {}).get("valueString"),
                        conexiones_bluetooth=document.fields.get("Conexiones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("Bluetooth", {}).get("valueString"),
                        conexiones_version_bluetooth=document.fields.get("Conexiones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("VersionBluetooth", {}).get("valueString"),
                        conexiones_thunderbolt=document.fields.get("Conexiones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("Thunderbolt", {}).get("valueString"),
                        conexiones_hdmi=document.fields.get("Conexiones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("HDMI", {}).get("valueString"),
                        conexiones_hdmi_micro=document.fields.get("Conexiones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("HDMIMicro", {}).get("valueString"),
                        conexiones_display_port=document.fields.get("Conexiones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("DisplayPort", {}).get("valueString"),
                        conexiones_mini_display_port=document.fields.get("Conexiones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("MiniDisplayPort", {}).get("valueString"),
                        conexiones_dockstation=document.fields.get("Conexiones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("ConextionDockStation", {}).get("valueString"),
                        conexiones_wireless=document.fields.get("Conexiones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("Wireless", {}).get("valueString"),
                        conexiones_puerto_carga=document.fields.get("Conexiones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("PuertoCarga", {}).get("valueString"),
                        conexiones_otras=document.fields.get("Conexiones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("OtrasConexiones", {}).get("valueString"),
                        ram_instalada=document.fields.get("RAM", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("RamInstalada", {}).get("valueString"),
                        ram_maxima=document.fields.get("RAM", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("RamMaxima", {}).get("valueString"),
                        ram_bancos_libres=document.fields.get("RAM", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("BancosRamLibres", {}).get("valueString"),
                        ram_velocidad=document.fields.get("RAM", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("VelocidadRam", {}).get("valueString"),
                        ram_tecnologia=document.fields.get("RAM", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("TecnologiaRam", {}).get("valueString"),
                        ram_tipo=document.fields.get("RAM", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("TipoRam", {}).get("valueString"),
                        tipologia_unidad=document.fields.get("TipologiaUnidad", {}).get("valueString"),
                        teclado_numerico=document.fields.get("Teclado", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("TecladoNumerico", {}).get("valueString"),
                        teclado_numero_teclas=document.fields.get("Teclado", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("NumeroTeclas", {}).get("valueString"),
                        teclado_retroiluminado=document.fields.get("Teclado", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("TecladoRetroiluminado", {}).get("valueString"),
                        audio_microfono_integrado=document.fields.get("Audio", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("MicrofonoIntegrado", {}).get("valueString"),
                        audio_fabricante_altavoces=document.fields.get("Audio", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("FabricanteAltavoces", {}).get("valueString"),
                        bateria_celdas=document.fields.get("Bateria", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("Celdas", {}).get("valueString"),
                        bateria_duracion=document.fields.get("Bateria", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("DuracionBateria", {}).get("valueString"),
                        webcam_integrada=document.fields.get("Webcam", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("WebcamIntegrada", {}).get("Webcam", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("Integrada", {}).get("valueString"),
                        webcam_resolucion=document.fields.get("Webcam", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("ResolucionWebcam", {}).get("valueString"),
                        webcam_infrarrojos=document.fields.get("Webcam", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("Infrarrojos", {}).get("valueString"),
                        webcam_tipo_camara_frontal=document.fields.get("Webcam", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("TipoCamaraFrontal", {}).get("valueString"),
                        lectores_memoria_compact_flash=document.fields.get("LectoresMemory", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("CompactFlash", {}).get("valueString"),
                        lectores_memoria_memory_stick=document.fields.get("LectoresMemory", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("MemoryStick", {}).get("valueString"),
                        lectores_memoria_memory_stick_duo=document.fields.get("LectoresMemory", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("MemoryStickDuo", {}).get("valueString"),
                        lectores_memoria_memory_stick_pro=document.fields.get("LectoresMemory", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("MemoryStickPro", {}).get("valueString"),
                        lectores_memoria_memory_stick_pro_duo=document.fields.get("LectoresMemory", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("MemoryStickProDuo", {}).get("valueString"),
                        lectores_memoria_memory_stick_pro_hg_duo=document.fields.get("LectoresMemory", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("MemoryStickProHG_Duo", {}).get("valueString"),
                        lectores_memoria_memory_stick_micro=document.fields.get("LectoresMemory", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("MemoryStickMicro", {}).get("valueString"),
                        lectores_memoria_micro_sd=document.fields.get("LectoresMemory", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("MicroSD", {}).get("valueString"),
                        lectores_memoria_multimedia_card=document.fields.get("LectoresMemory", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("MultimediaCard", {}).get("valueString"),
                        lectores_memoria_mmc_plus=document.fields.get("LectoresMemory", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("MMCPlus", {}).get("valueString"),
                        lectores_memoria_multimedia_card_reduced_size=document.fields.get("LectoresMemory", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("MultimediaCardReducedSize", {}).get("valueString"),
                        lectores_memoria_secure_digital_card=document.fields.get("LectoresMemory", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("SecureDigitalCard", {}).get("valueString"),
                        lectores_memoria_secure_digital_mini=document.fields.get("LectoresMemory", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("SecureDigitalMini", {}).get("valueString"),
                        sistema_software_version_so=document.fields.get("SistemaYSoftware", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("VersionSO", {}).get("valueString"),
                        sistema_software_bits_so=document.fields.get("SistemaYSoftware", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("BitSO", {}).get("valueString"),
                        sistema_software_software_incluido=document.fields.get("SistemaYSoftware", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("SoftwareIncluido", {}).get("valueString"),
                        soluciones=document.fields.get("Soluciones", {}).get("valueString"),
                        size_embalaje_lado_a=document.fields.get("TamañoEmbalaje", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("LadoA", {}).get("valueString"),
                        size_embalaje_lado_b=document.fields.get("TamañoEmbalaje", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("LadoB", {}).get("valueString"),
                        size_embalaje_lado_c=document.fields.get("TamañoEmbalaje", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("LadoC", {}).get("valueString"),
                        size_embalaje_peso=document.fields.get("TamañoEmbalaje", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("Peso", {}).get("valueString"),
                        certificaciones_energy_star=document.fields.get("Certificaciones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("EnergyStar", {}).get("valueString"),
                        certificaciones_wifi=document.fields.get("Certificaciones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("WiFi", {}).get("valueString"),
                        certificaciones_otras=document.fields.get("Certificaciones", {}).get("valueArray", [{}])[0].get("valueObject", {}).get("Otras", {}).get("valueString"),
                        descripcion=document.fields.get("Descripcion", {}).get("valueString")
                    )

                save_append(document_object.to_dict())
            
            return JsonResponse({"status": "success", "message": "PDF uploaded and processed successfully."})

        else:
            return JsonResponse({"status": "error", "message": "No file uploaded."}, status=400)

    except Exception as e:
        logging.error(f"Error occurred: {e} Container: {os.getenv('BLOB_UPLOADS_CONTAINER_NAME')}")
        return JsonResponse({"status": "error", "message": f"Error occurred: {str(e)}"}, status=500)


def save(document):
    data.append(document.to_dict())
    save_to_json()

def save_append(analyze_layout_response):
    try:
        # Read the existing data from the JSON file if it exists
        try:
            with open("processed_data.json", "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            data = []  # If the file doesn't exist, initialize an empty list

        # Append the new analyze layout response
        data.append(analyze_layout_response)

        # Save the updated data back to the JSON file
        with open("processed_data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

    except Exception as e:
        # Handle any exceptions
        print(f"Error saving or appending data: {e}")

def save_to_json():
    with open("processed_data.json", "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)

def send_message(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        if not query:
            return JsonResponse({'error': 'No query provided'}, status=400)

    try:
        ls_prediction_endpoint = os.getenv('LS_CONVERSATIONS_ENDPOINT')
        ls_prediction_key = os.getenv('LS_CONVERSATIONS_KEY')

        if not ls_prediction_endpoint or not ls_prediction_key:
            raise ValueError("LS_CONVERSATIONS_ENDPOINT or LS_CONVERSATIONS_KEY not found.")

        client = ConversationAnalysisClient(
            ls_prediction_endpoint, 
            AzureKeyCredential(ls_prediction_key)
        )

        cls_project = os.getenv('LS_CONVERSATIONS_PROJECT')
        deployment_slot = os.getenv('LS_CONVERSATIONS_DEPLOYMENT_SLOT')

        result = client.analyze_conversation(
            task={
                "kind": "Conversation",
                "analysisInput": {
                    "conversationItem": {
                        "participantId": "1",
                        "id": "1",
                        "modality": "text",
                        "language": "en",
                        "text": query
                    },
                    "isLoggingEnabled": False
                },
                "parameters": {
                    "projectName": cls_project,
                    "deploymentName": deployment_slot,
                    "verbose": True
                }
            }
        )

        if "result" in result and "prediction" in result["result"]:
            top_intent = result["result"]["prediction"]["topIntent"]
            entities = result["result"]["prediction"].get("entities", [])

            print(f"Top Intent: {top_intent}")
            print(f"Entities: {entities}")

            return JsonResponse(result)

        else:
            return JsonResponse({"error": "Unexpected response structure."}, status=500)

    except Exception as ex:
        print(f"An error occurred: {ex}")
        return JsonResponse({"error": str(ex)}, status=500)

class Home(TemplateView):
    template_name="index.html"

    def get_context_data(self, **kwargs):

        with open("processed_data.json", "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

        context = super(Home, self).get_context_data(**kwargs)
        context['items'] = data

        return context

class InspectItem(TemplateView):
    template_name="inspect_item.html"

    def get_context_data(self, **kwargs):
        code_from_url = self.kwargs.get("code")

        with open("processed_data.json", "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

        matching_item = next((item for item in data if item.get("codigo_producto") == code_from_url), None)

        context = super().get_context_data(**kwargs)
        context["item"] = matching_item

        return context