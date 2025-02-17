class Document:
    def __init__(self, empresa, direccion_empresa, producto, codigo_producto, precio, garantia, disco_disco, disco_capacidad, disco_tipo_soporte, disco_interfaz_soporte, disco_velocidad_soporte, disco_numero_soportes, gpu_integrada, gpu_fabricante, gpu_modelo, gpu_memoria, cpu_familia, cpu_modelo, cpu_fabricante, cpu_generacion, cpu_nucleos, cpu_frecuencia, cpu_frecuencia_turbo, pantalla_size, pantalla_tactil, pantalla_tipo, pantalla_resolucion, pantalla_luminosidad, pantalla_contraste, pantalla_tipologia_hd, pantalla_retroiluminacion, pantalla_relacion_aspecto, pantalla_tiempo_maximo_refresco, pantalla_espacio_rgb, pantalla_superficie, dimensiones_peso, dimensiones_altura, dimensiones_ancho, dimensiones_profundidad, general_color, general_tpm, general_material_chasis, general_deteccion_huella, general_potencia_adaptador_ac, general_2_en_1_detachable, conexiones_red_movil, conexiones_total_usb, conexiones_usb_2_0, conexiones_usb_3_2, conexiones_ethernet, conexiones_vga, conexiones_bluetooth, conexiones_version_bluetooth, conexiones_thunderbolt, conexiones_hdmi, conexiones_hdmi_micro, conexiones_display_port, conexiones_mini_display_port, conexiones_dockstation, conexiones_wireless, conexiones_puerto_carga, conexiones_otras, ram_instalada, ram_maxima, ram_bancos_libres, ram_velocidad, ram_tecnologia, ram_tipo, tipologia_unidad, teclado_numerico, teclado_numero_teclas, teclado_retroiluminado, audio_microfono_integrado, audio_fabricante_altavoces, bateria_celdas, bateria_duracion, webcam_integrada, webcam_resolucion, webcam_infrarrojos, webcam_tipo_camara_frontal, lectores_memoria_compact_flash, lectores_memoria_memory_stick, lectores_memoria_memory_stick_duo, lectores_memoria_memory_stick_pro, lectores_memoria_memory_stick_pro_duo, lectores_memoria_memory_stick_pro_hg_duo, lectores_memoria_memory_stick_micro, lectores_memoria_micro_sd, lectores_memoria_multimedia_card, lectores_memoria_mmc_plus, lectores_memoria_multimedia_card_reduced_size, lectores_memoria_secure_digital_card, lectores_memoria_secure_digital_mini, sistema_software_version_so, sistema_software_bits_so, sistema_software_software_incluido, soluciones, size_embalaje_lado_a, size_embalaje_lado_b, size_embalaje_lado_c, size_embalaje_peso, certificaciones_energy_star, certificaciones_wifi, certificaciones_otras, descripcion):
        self.empresa = empresa
        self.direccion_empresa = direccion_empresa
        self.producto = producto
        self.codigo_producto = codigo_producto.replace("Código: ", "")
        self.precio = precio
        self.garantia = garantia.replace("Garantía: ", "")
        self.disco_disco = disco_disco
        self.disco_capacidad = disco_capacidad
        self.disco_tipo_soporte = disco_tipo_soporte
        self.disco_interfaz_soporte = disco_interfaz_soporte
        self.disco_velocidad_soporte = disco_velocidad_soporte
        self.disco_numero_soportes = disco_numero_soportes
        self.gpu_integrada = gpu_integrada
        self.gpu_fabricante = gpu_fabricante
        self.gpu_modelo = gpu_modelo
        self.gpu_memoria = gpu_memoria
        self.cpu_familia = cpu_familia
        self.cpu_modelo = cpu_modelo
        self.cpu_fabricante = cpu_fabricante
        self.cpu_generacion = cpu_generacion
        self.cpu_nucleos = cpu_nucleos
        self.cpu_frecuencia = cpu_frecuencia
        self.cpu_frecuencia_turbo = cpu_frecuencia_turbo
        self.pantalla_size = pantalla_size
        self.pantalla_tactil = pantalla_tactil
        self.pantalla_tipo = pantalla_tipo
        self.pantalla_resolucion = pantalla_resolucion
        self.pantalla_luminosidad = pantalla_luminosidad
        self.pantalla_contraste = pantalla_contraste
        self.pantalla_tipologia_hd = pantalla_tipologia_hd
        self.pantalla_retroiluminacion = pantalla_retroiluminacion
        self.pantalla_relacion_aspecto = pantalla_relacion_aspecto
        self.pantalla_tiempo_maximo_refresco = pantalla_tiempo_maximo_refresco
        self.pantalla_espacio_rgb = pantalla_espacio_rgb
        self.pantalla_superficie = pantalla_superficie
        self.dimensiones_peso = dimensiones_peso
        self.dimensiones_altura = dimensiones_altura
        self.dimensiones_ancho = dimensiones_ancho
        self.dimensiones_profundidad = dimensiones_profundidad
        self.general_color = general_color
        self.general_tpm = general_tpm
        self.general_material_chasis = general_material_chasis
        self.general_deteccion_huella = general_deteccion_huella
        self.general_potencia_adaptador_ac = general_potencia_adaptador_ac
        self.general_2_en_1_detachable = general_2_en_1_detachable
        self.conexiones_red_movil = conexiones_red_movil
        self.conexiones_total_usb = conexiones_total_usb
        self.conexiones_usb_2_0 = conexiones_usb_2_0
        self.conexiones_usb_3_2 = conexiones_usb_3_2
        self.conexiones_ethernet = conexiones_ethernet
        self.conexiones_vga = conexiones_vga
        self.conexiones_bluetooth = conexiones_bluetooth
        self.conexiones_version_bluetooth = conexiones_version_bluetooth
        self.conexiones_thunderbolt = conexiones_thunderbolt
        self.conexiones_hdmi = conexiones_hdmi
        self.conexiones_hdmi_micro = conexiones_hdmi_micro
        self.conexiones_display_port = conexiones_display_port
        self.conexiones_mini_display_port = conexiones_mini_display_port
        self.conexiones_dockstation = conexiones_dockstation
        self.conexiones_wireless = conexiones_wireless
        self.conexiones_puerto_carga = conexiones_puerto_carga
        self.conexiones_otras = conexiones_otras
        self.ram_instalada = ram_instalada
        self.ram_maxima = ram_maxima
        self.ram_bancos_libres = ram_bancos_libres
        self.ram_velocidad = ram_velocidad
        self.ram_tecnologia = ram_tecnologia
        self.ram_tipo = ram_tipo
        self.tipologia_unidad = tipologia_unidad
        self.teclado_numerico = teclado_numerico
        self.teclado_numero_teclas = teclado_numero_teclas
        self.teclado_retroiluminado = teclado_retroiluminado
        self.audio_microfono_integrado = audio_microfono_integrado
        self.audio_fabricante_altavoces = audio_fabricante_altavoces
        self.bateria_celdas = bateria_celdas
        self.bateria_duracion = bateria_duracion
        self.webcam_integrada = webcam_integrada
        self.webcam_resolucion = webcam_resolucion
        self.webcam_infrarrojos = webcam_infrarrojos
        self.webcam_tipo_camara_frontal = webcam_tipo_camara_frontal
        self.lectores_memoria_compact_flash = lectores_memoria_compact_flash
        self.lectores_memoria_memory_stick = lectores_memoria_memory_stick
        self.lectores_memoria_memory_stick_duo = lectores_memoria_memory_stick_duo
        self.lectores_memoria_memory_stick_pro = lectores_memoria_memory_stick_pro
        self.lectores_memoria_memory_stick_pro_duo = lectores_memoria_memory_stick_pro_duo
        self.lectores_memoria_memory_stick_pro_hg_duo = lectores_memoria_memory_stick_pro_hg_duo
        self.lectores_memoria_memory_stick_micro = lectores_memoria_memory_stick_micro
        self.lectores_memoria_micro_sd = lectores_memoria_micro_sd
        self.lectores_memoria_multimedia_card = lectores_memoria_multimedia_card
        self.lectores_memoria_mmc_plus = lectores_memoria_mmc_plus
        self.lectores_memoria_multimedia_card_reduced_size = lectores_memoria_multimedia_card_reduced_size
        self.lectores_memoria_secure_digital_card = lectores_memoria_secure_digital_card
        self.lectores_memoria_secure_digital_mini = lectores_memoria_secure_digital_mini
        self.sistema_software_version_so = sistema_software_version_so
        self.sistema_software_bits_so = sistema_software_bits_so
        self.sistema_software_software_incluido = sistema_software_software_incluido
        self.soluciones = soluciones
        self.size_embalaje_lado_a = size_embalaje_lado_a
        self.size_embalaje_lado_b = size_embalaje_lado_b
        self.size_embalaje_lado_c = size_embalaje_lado_c
        self.size_embalaje_peso = size_embalaje_peso
        self.certificaciones_energy_star = certificaciones_energy_star
        self.certificaciones_wifi = certificaciones_wifi
        self.certificaciones_otras = certificaciones_otras
        self.descripcion = descripcion

    def to_dict(self):
        document_dict = {
            "empresa": self.empresa,
            "direccion_empresa": self.direccion_empresa,
            "producto": self.producto,
            "codigo_producto": self.codigo_producto,
            "precio": self.precio,
            "garantia": self.garantia,
            "disco_disco": self.disco_disco,
            "disco_capacidad": self.disco_capacidad,
            "disco_tipo_soporte": self.disco_tipo_soporte,
            "disco_interfaz_soporte": self.disco_interfaz_soporte,
            "disco_velocidad_soporte": self.disco_velocidad_soporte,
            "disco_numero_soportes": self.disco_numero_soportes,
            "gpu_integrada": self.gpu_integrada,
            "gpu_fabricante": self.gpu_fabricante,
            "gpu_modelo": self.gpu_modelo,
            "gpu_memoria": self.gpu_memoria,
            "cpu_familia": self.cpu_familia,
            "cpu_modelo": self.cpu_modelo,
            "cpu_fabricante": self.cpu_fabricante,
            "cpu_generacion": self.cpu_generacion,
            "cpu_nucleos": self.cpu_nucleos,
            "cpu_frecuencia": self.cpu_frecuencia,
            "cpu_frecuencia_turbo": self.cpu_frecuencia_turbo,
            "pantalla_size": self.pantalla_size,
            "pantalla_tactil": self.pantalla_tactil,
            "pantalla_tipo": self.pantalla_tipo,
            "pantalla_resolucion": self.pantalla_resolucion,
            "pantalla_luminosidad": self.pantalla_luminosidad,
            "pantalla_contraste": self.pantalla_contraste,
            "pantalla_tipologia_hd": self.pantalla_tipologia_hd,
            "pantalla_retroiluminacion": self.pantalla_retroiluminacion,
            "pantalla_relacion_aspecto": self.pantalla_relacion_aspecto,
            "pantalla_tiempo_maximo_refresco": self.pantalla_tiempo_maximo_refresco,
            "pantalla_espacio_rgb": self.pantalla_espacio_rgb,
            "pantalla_superficie": self.pantalla_superficie,
            "dimensiones_peso": self.dimensiones_peso,
            "dimensiones_altura": self.dimensiones_altura,
            "dimensiones_ancho": self.dimensiones_ancho,
            "dimensiones_profundidad": self.dimensiones_profundidad,
            "general_color": self.general_color,
            "general_tpm": self.general_tpm,
            "general_material_chasis": self.general_material_chasis,
            "general_deteccion_huella": self.general_deteccion_huella,
            "general_potencia_adaptador_ac": self.general_potencia_adaptador_ac,
            "general_2_en_1_detachable": self.general_2_en_1_detachable,
            "conexiones_red_movil": self.conexiones_red_movil,
            "conexiones_total_usb": self.conexiones_total_usb,
            "conexiones_usb_2_0": self.conexiones_usb_2_0,
            "conexiones_usb_3_2": self.conexiones_usb_3_2,
            "conexiones_ethernet": self.conexiones_ethernet,
            "conexiones_vga": self.conexiones_vga,
            "conexiones_bluetooth": self.conexiones_bluetooth,
            "conexiones_version_bluetooth": self.conexiones_version_bluetooth,
            "conexiones_thunderbolt": self.conexiones_thunderbolt,
            "conexiones_hdmi": self.conexiones_hdmi,
            "conexiones_hdmi_micro": self.conexiones_hdmi_micro,
            "conexiones_display_port": self.conexiones_display_port,
            "conexiones_mini_display_port": self.conexiones_mini_display_port,
            "conexiones_dockstation": self.conexiones_dockstation,
            "conexiones_wireless": self.conexiones_wireless,
            "conexiones_puerto_carga": self.conexiones_puerto_carga,
            "conexiones_otras": self.conexiones_otras,
            "ram_instalada": self.ram_instalada,
            "ram_maxima": self.ram_maxima,
            "ram_bancos_libres": self.ram_bancos_libres,
            "ram_velocidad": self.ram_velocidad,
            "ram_tecnologia": self.ram_tecnologia,
            "ram_tipo": self.ram_tipo,
            "tipologia_unidad": self.tipologia_unidad,
            "teclado_numerico": self.teclado_numerico,
            "teclado_numero_teclas": self.teclado_numero_teclas,
            "teclado_retroiluminado": self.teclado_retroiluminado,
            "audio_microfono_integrado": self.audio_microfono_integrado,
            "audio_fabricante_altavoces": self.audio_fabricante_altavoces,
            "bateria_celdas": self.bateria_celdas,
            "bateria_duracion": self.bateria_duracion,
            "webcam_integrada": self.webcam_integrada,
            "webcam_resolucion": self.webcam_resolucion,
            "webcam_infrarrojos": self.webcam_infrarrojos,
            "webcam_tipo_camara_frontal": self.webcam_tipo_camara_frontal,
            "lectores_memoria_compact_flash": self.lectores_memoria_compact_flash,
            "lectores_memoria_memory_stick": self.lectores_memoria_memory_stick,
            "lectores_memoria_memory_stick_duo": self.lectores_memoria_memory_stick_duo,
            "lectores_memoria_memory_stick_pro": self.lectores_memoria_memory_stick_pro,
            "lectores_memoria_memory_stick_pro_duo": self.lectores_memoria_memory_stick_pro_duo,
            "lectores_memoria_memory_stick_pro_hg_duo": self.lectores_memoria_memory_stick_pro_hg_duo,
            "lectores_memoria_memory_stick_micro": self.lectores_memoria_memory_stick_micro,
            "lectores_memoria_micro_sd": self.lectores_memoria_micro_sd,
            "lectores_memoria_multimedia_card": self.lectores_memoria_multimedia_card,
            "lectores_memoria_mmc_plus": self.lectores_memoria_mmc_plus,
            "lectores_memoria_multimedia_card_reduced_size": self.lectores_memoria_multimedia_card_reduced_size,
            "lectores_memoria_secure_digital_card": self.lectores_memoria_secure_digital_card,
            "lectores_memoria_secure_digital_mini": self.lectores_memoria_secure_digital_mini,
            "sistema_software_version_so": self.sistema_software_version_so,
            "sistema_software_bits_so": self.sistema_software_bits_so,
            "sistema_software_software_incluido": self.sistema_software_software_incluido,
            "soluciones": self.soluciones,
            "size_embalaje_lado_a": self.size_embalaje_lado_a,
            "size_embalaje_lado_b": self.size_embalaje_lado_b,
            "size_embalaje_lado_c": self.size_embalaje_lado_c,
            "size_embalaje_peso": self.size_embalaje_peso,
            "certificaciones_energy_star": self.certificaciones_energy_star,
            "certificaciones_wifi": self.certificaciones_wifi,
            "certificaciones_otras": self.certificaciones_otras,
            "descripcion": self.descripcion
        }

        return document_dict