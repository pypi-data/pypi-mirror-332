import streamlit as st
import pandas as pd
import numpy as np
from streamlit_js_eval import streamlit_js_eval


class EchartCalculator:
    def __init__(self):
        if "show_res" not in st.session_state:
            st.session_state["show_res"] = False
        self.page_width = streamlit_js_eval(
            js_expressions="parent.document.getElementsByClassName('stSidebar')[0].clientWidth",
            key="WIDTH",
            want_output=True,
        )
        with st.sidebar:
            self.calc_container = st.container()
            with self.calc_container:
                self.res_container = st.container()

    def _trigger_res(self):
        print(st.session_state["show_res"])
        st.session_state["show_res"] = not st.session_state["show_res"]

    def inject_content(self):
        with self.calc_container:
            st.write("📝 Calculator", self.page_width)
            price = st.slider("Price", 0, 130, 25)
            flat = st.slider("Flat rate", 0, 130, 25)
            profit = st.slider("Profit", 0, 130, 25)
            st.button(
                "Submit",
                on_click=self._trigger_res,
            )
        self.calc_container.float(
            f"position:fixed; bottom: 0; width: {self.page_width}px; margin-bottom: 10px"
        )

        if (
            "show_res" in st.session_state
            and st.session_state["show_res"]
            and not st.session_state[self.renderKey]
        ):
            with self.res_container:
                chart_data = pd.DataFrame(
                    np.random.randn(20, 3), columns=["a", "b", "c"]
                )
                st.line_chart(
                    chart_data, width=600, use_container_width=False, height=400
                )
            self.res_container.float(
                f"position: absolute; background-color: white; left: 100%; bottom: 0%; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); border-radius: 10px;box-sizing:content-box;padding: 30px; width: 600px; height:450px;z-index:999999;"
            )
