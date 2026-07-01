import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Proyecto Fundamentos Científicos - UCSUR", layout="wide")

st.title("Cinemática: Análisis de la Velocidad y la Distancia de Frenado")
st.subheader("Prevención de accidentes en carreteras de la Sierra peruana")

menu = st.sidebar.selectbox("Secciones", ["Introducción General", "Fundamento Teórico", "Metodología", "Resultados", "Conclusiones"])

if menu == "Introducción General":
    st.title("🌐 Introducción General")
    st.markdown("---")

    tab1, tab2, tab3 = st.tabs(["📍 Contexto y Problemática", "🔍 Fundamentos", "🚀 Propósito del Estudio"])

    with tab1:
        st.subheader("El desafío de las carreteras de la Sierra")
        col1, col2 = st.columns(2)
        with col1:
            st.info("**Contexto:** Las carreteras de la Sierra peruana atraviesan zonas montañosas con pendientes pronunciadas, curvas cerradas y cambios climáticos constantes, desafiando la capacidad de reacción del conductor.")
        with col2:
            st.warning("**Problemática:** El exceso de velocidad y la insuficiente distancia de frenado son causas críticas de accidentes, exigiendo una comprensión profunda de los principios físicos en juego.")

    with tab2:
        st.subheader("Marco Teórico y Enfoque")
        with st.expander("Ver Definición de Cinemática"):
            st.write("La cinemática es la rama de la física que estudia el movimiento de los cuerpos a través de magnitudes como la posición, la trayectoria, la velocidad y la aceleración, sin analizar las fuerzas que lo producen.")
        
        st.write("🛠️ **Enfoque del estudio:** La investigación adopta un enfoque experimental utilizando una maqueta que representa las condiciones de las carreteras andinas para analizar la relación entre velocidad y frenado.")

    with tab3:
        st.success("### 🎯 Objetivo General")
        st.write("Analizar la influencia de la velocidad en la distancia de frenado mediante los principios de la cinemática, con el propósito de promover la prevención de accidentes.")
        
        with st.expander("📋 Ver Objetivos Específicos"):
            st.write("- Comprender los conceptos fundamentales de la cinemática.")
            st.write("- Determinar la relación entre la velocidad y la distancia de frenado.")
            st.write("- Aplicar procedimientos experimentales mediante una maqueta.")
            st.write("- Interpretar resultados para proponer medidas de seguridad vial.")

    st.markdown("---")
    
    with st.container():
        st.markdown("### 📚 Justificación del estudio")
        st.write("Este estudio busca fortalecer la conciencia sobre la importancia de conducir a velocidades adecuadas, contribuyendo a la promoción de prácticas responsables para la prevención de accidentes.")

    st.markdown("**Palabras clave:**")
    tags = ["Cinemática", "Velocidad", "Distancia de frenado", "Seguridad vial", "Accidentes", "Sierra peruana"]
    cols = st.columns(len(tags))
    for i, tag in enumerate(tags):
        cols[i].caption(f"🏷️ {tag}")

elif menu == "Fundamento Teórico":
    st.title("📚 Fundamento Teórico")
    st.markdown("La base cinemática que sustenta nuestro análisis experimental.")
    st.markdown("---")

    with st.expander("🔍 1. Conceptos Básicos (Posición, Trayectoria y Distancia)", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### Cinemática")
            st.write("Estudia el movimiento (posición, velocidad, aceleración) sin considerar fuerzas.")
            st.latex(r"v = \frac{\Delta x}{\Delta t}")
            
            st.markdown("### Posición y Trayectoria")
            st.write("La **posición** define el lugar respecto a un sistema de referencia. La **trayectoria** es el camino recorrido, complejo en la Sierra debido a curvas y pendientes.")
        
        with col2:
            st.markdown("### Distancia vs. Desplazamiento")
            st.write("La **distancia ($d$)** es la longitud total del camino (magnitud escalar). El **desplazamiento ($\Delta x$)** es el cambio neto de posición (vectorial).")
            st.latex(r"d = \sum d_i \quad | \quad \Delta x = x_f - x_i")

    with st.expander("📈 2. Magnitudes de Movimiento (Rapidez, Velocidad y Aceleración)"):
        col_r, col_v, col_a = st.columns(3)
        
        with col_r:
            st.markdown("### 🏃 Rapidez Media ($R_m$)")
            st.write("Es una magnitud **escalar**. Indica qué tan rápido se recorre una distancia total respecto al tiempo, sin importar hacia dónde se dirija el vehículo.")
            st.latex(r"R_m = \frac{d}{\Delta t}")
            
        with col_v:
            st.markdown("### 🏎️ Velocidad Media ($V_m$)")
            st.write("Es una magnitud **vectorial**. Relaciona el desplazamiento (cambio de posición) con el tiempo. Aquí **sí importa la dirección** del movimiento.")
            st.latex(r"V_m = \frac{\Delta x}{\Delta t}")
            
        with col_a:
            st.markdown("### 🚀 Aceleración Media ($a_m$)")
            st.write("Mide cómo cambia la velocidad en el tiempo. Es vital al **frenar**: cuando el vehículo reduce su velocidad, la aceleración es negativa.")
            st.latex(r"a_m = \frac{\Delta v}{\Delta t}")
            
        st.info("💡 **Nota para el experimento:** En la Sierra, la aceleración media al frenar variará según la pendiente de la carretera simulada en la maqueta.")

    with st.expander("⚡ 3. Modelo MRUV (Aceleración Constante)"):
        st.write("Útil para analizar procesos de aceleración y frenado idealizados:")
        st.latex(r"v_f = v_i + at")
        st.latex(r"x = x_0 + v_it + \frac{1}{2}at^2")
        st.latex(r"v_f^2 = v_i^2 + 2a\Delta x")

    with st.expander("🛑 4. Distancia de Detención y Seguridad Vial", expanded=True):
        st.write("La distancia total es crítica para prevenir accidentes en la Sierra:")
        
        col_r, col_f = st.columns(2)
        with col_r:
            st.info("### Distancia de Reacción")
            st.write("Espacio recorrido mientras el conductor percibe el peligro.")
            st.latex(r"d_r = v \cdot t_r")
        with col_f:
            st.warning("### Distancia de Frenado")
            st.write("Espacio necesario para detener el vehículo tras frenar.")
            st.latex(r"d_f = \frac{v^2}{2|a|}")
            
        st.success("### Distancia Total de Detención")
        st.latex(r"d_t = d_r + d_f")
        st.write("El cuadrado de la velocidad en la fórmula de frenado demuestra por qué el exceso de velocidad incrementa exponencialmente el riesgo.")

    st.markdown("---")
    st.write("💡 **Aplicación en la Sierra:** En entornos montañosos, las condiciones variables hacen que el control de la velocidad sea la herramienta clave para minimizar la distancia total de detención.")

elif menu == "Metodología":
    st.title("⚙️ Metodología y Método Científico")
    
    tab1, tab2 = st.tabs(["📊 Enfoque de Investigación", "🧪 Aplicación del Método Científico"])
    
    with tab1:
        st.write("Nuestro estudio integra tres pilares fundamentales:")
        col1, col2, col3 = st.columns(3)
        col1.metric("Experimental", "Manipulación de variables")
        col2.metric("Aplicada", "Solución a problemas reales")
        col3.metric("Cuantitativa", "Análisis de datos numéricos")
        
    with tab2:
        steps = ["Observación", "Planteamiento del Problema", "Hipótesis", "Experimentación", "Análisis de Resultados", "Conclusiones"]
        step_selected = st.select_slider("Etapas del Método Científico", options=steps)
        
        if step_selected == "Observación":
            st.info("Se observa que las carreteras de la Sierra peruana presentan características geográficas complejas, como curvas pronunciadas y pendientes, que incrementan el riesgo de accidentes cuando los vehículos circulan a velocidades elevadas.")
        elif step_selected == "Planteamiento del Problema":
            st.success("¿Cómo influye la velocidad de un vehículo en la distancia de frenado y en la prevención de accidentes en las carreteras de la Sierra peruana?")
        elif step_selected == "Hipótesis":
            st.info("Si la velocidad del vehículo aumenta, entonces la distancia de frenado también aumentará significativamente, incrementando el riesgo de accidentes en las vías de la Sierra peruana.")
        elif step_selected == "Experimentación":
            st.success("Se realizaron pruebas utilizando una maqueta representativa de una carretera andina. El vehículo fue desplazado a diferentes velocidades y se registró la distancia necesaria para lograr su detención en cada ensayo.")
        elif step_selected == "Análisis de Resultados":
            st.info("Se realizaron pruebas utilizando una maqueta representativa de una carretera andina. El vehículo fue desplazado a diferentes velocidades y se registró la distancia necesaria para lograr su detención en cada ensayo.")
        elif step_selected == "Conclusiones":
            st.success("Finalmente, se evaluó la validez de la hipótesis planteada y se establecieron recomendaciones orientadas a fortalecer la seguridad vial y la conducción responsable en zonas montañosas.")

    st.markdown("---")
    st.subheader("⚖️ Variables del Experimento")
    v1, v2, v3 = st.columns(3)

    with v1:
        st.metric(
            label="🔹 Independiente", 
            value="Velocidad (m/s)", 
            help="Es la variable que se modifica deliberadamente durante el experimento para analizar sus efectos sobre el proceso de frenado."
        )
        st.write("*Variable que se modifica para observar sus efectos.*")

    with v2:
        st.metric(
            label="🔹 Dependiente", 
            value="Distancia (cm)", 
            help="Corresponde a la magnitud que se mide y que varía en función de la velocidad inicial del vehículo."
        )
        st.write("*Magnitud medida que cambia según la velocidad.*")

    with v3:
        st.markdown("**🔹 Variables Controladas**")
        st.markdown("""
            <div style="background-color: #f8fafc; padding: 10px; border-radius: 5px; border-left: 3px solid #64748b; font-size: 14px; color: #475569;">
                Factores mantenidos constantes para garantizar la validez de los resultados:
                <ul style="margin-top: 5px; margin-bottom: 0px;">
                    <li>Pendiente de la rampa</li>
                    <li>Tipo de superficie</li>
                    <li>Masa del vehículo</li>
                    <li>Sistema de frenado</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    with st.expander("🛠️ Materiales y Procedimiento Experimental"):
        col_m, col_p = st.columns(2)
        with col_m:
            st.markdown("### Lista de Materiales")
            st.write("- Maqueta de carretera andina\n- Vehículo de prueba\n- Cronómetro y cinta métrica\n- Rampa controlada")
        with col_p:
            st.markdown("### Procedimiento")
            st.write("1. Construcción de maqueta con pendiente controlada.\n2. Definición de velocidades iniciales.\n3. Registro de distancias de frenado.\n4. Repetición de ensayos para reducir error.")

    st.info("💡 **Nota:** Todo este proceso cumple con el ciclo de registro, organización y análisis de datos experimentales.")

elif menu == "Resultados":
    st.title("📊 Resultados y Análisis")
    st.markdown("Análisis de la relación entre la velocidad inicial y la capacidad de detención.")
    st.markdown("---")

    st.subheader("4.1. Registro de Datos")
    with st.container():
        st.write("Datos recopilados en la maqueta simulando una carretera de la Sierra:")
        
        import pandas as pd
        data = {
            "Ensayo": [1, 2, 3, 4, 5],
            "Velocidad (m/s)": [1.5, 2.2, 3.0, 3.8, 4.5],
            "Tiempo Frenado (s)": [0.8, 1.1, 1.4, 1.8, 2.1],
            "Distancia Frenado (cm)": [25, 48, 81, 125, 182]
        }
        df = pd.DataFrame(data)
        st.table(df) 

    st.subheader("4.2. Tendencias y Comportamiento")
    col_graph, col_interp = st.columns([0.6, 0.4])
    
    with col_graph:
        st.line_chart(df.set_index("Velocidad (m/s)")["Distancia Frenado (cm)"])
        st.caption("Gráfico: Relación Velocidad vs. Distancia de Frenado")

    with col_interp:
        st.info("### 🧐 Interpretación")
        st.write("""
        Se observa que el crecimiento de la distancia de frenado **no es lineal**, sino que aumenta de manera acelerada. 
        Esto confirma la teoría: si duplicas la velocidad, la distancia de frenado se cuadruplica.
        """)

    st.markdown("---")
    st.subheader("4.3. Comparación con la Hipótesis")
    
    st.success("""
    **Hipótesis Aceptada:** La evidencia experimental demuestra que pequeños aumentos en la velocidad generan incrementos significativos en la distancia de frenado. 
    Esto valida que la velocidad es el factor determinante en la seguridad vial en zonas montañosas.
    """)

    st.warning("⚠️ **Conclusión Crítica:** En la Sierra peruana, el margen de maniobra se reduce drásticamente con cada m/s de exceso de velocidad.")

elif menu == "Conclusiones":
    st.title("🏁 Conclusiones y Futuro")
    st.markdown("Cierre del análisis y recomendaciones para la seguridad en las carreteras andinas.")
    st.markdown("---")

    st.subheader("5.1. Conclusiones Científicas")
    with st.container():
        col_c1, col_c2 = st.columns(2)
        with col_c1:
            st.success("""
            **Validación Teórica**
            * Los principios de la cinemática describen con precisión el movimiento mediante la posición, velocidad y aceleración.
            * Se comprobó que la distancia de frenado aumenta al incrementar la velocidad inicial.
            """)
        with col_c2:
            st.success("""
            **Comportamiento Físico**
            * La relación **no es lineal**; a mayor velocidad, el incremento del espacio de frenado es exponencial.
            * El modelamiento matemático es vital para entender problemas de seguridad vial en el mundo real.
            """)

    st.markdown("---")
    st.subheader("🚀 Recomendaciones para la Prevención")
    st.info("Acciones clave para conductores y autoridades en la Sierra peruana:")
    
    r1, r2, r3 = st.columns(3)
    r1.markdown("🛑 **Velocidad:** Respetar límites y reducir rapidez en curvas o baja visibilidad.")
    r2.markdown("📢 **Educación:** Promover campañas sobre la relación entre velocidad y distancia de frenado.")
    r3.markdown("🛠️ **Mantenimiento:** Fomentar el chequeo periódico de frenos y neumáticos.")
    
    with st.expander("Ver más recomendaciones técnicas"):
        st.write("- Fortalecer la señalización preventiva en tramos de alta peligrosidad.")
        st.write("- Integrar conceptos de física en la formación de nuevos conductores.")

    st.markdown("---")
    with st.expander("🔮 Trabajo Futuro y Mejoras"):
        st.write("""
        Para elevar el rigor de este proyecto, en futuras etapas se planea:
        1. **Nuevas Variables:** Incorporar clima (lluvia/hielo), estado del pavimento e inclinación exacta del terreno.
        2. **Simulación Digital:** Implementar software de simulación para contrastar la maqueta física con modelos computacionales.
        3. **Masa Dinámica:** Analizar cómo influye la carga del vehículo (pasajeros/mercancía) en la inercia de frenado.
        """)

    st.markdown("---")
    st.caption("Investigación realizada bajo los lineamientos de Fundamentos Científicos - UCSUR 2026.")
