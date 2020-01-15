# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 15:52:42 2020

@author: Евгений
"""

import plotly.graph_objects as go

fig = go.Figure(
    go.Waterfall(
        name="2018",
        orientation="h",
        measure=[
            "relative",
            "relative",
            "relative",
            "relative",
            "relative",
            "relative",
            "relative",
        ],
        y=[
            "Выпуск",
            "Импорт",
            "Потребление",
            "Инвестиции",
            "Экспорт",
            "Ошибка",          
            "Промежуточное портебление",
        ],
        x=[196.6, 21.6, -69.3, -23.6,  -31.9, -0.6, -92.7, ],
        connector={
            "mode": "between",
            "line": {"width": 4, "color": "rgb(0, 0, 0)", "dash": "solid"},
        },
    )
)


fig.update_layout(title="Profit and loss statement 2018")

fig.write_html("first_figure.html", auto_open=True)

fig.show()
