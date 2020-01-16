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
            "Статистическое расхождение",
            "Экспорт",
            "Инвестиции",
            "Конечное потребление",
            "Промежуточное потребление",
        ],
        x=[196.6, 21.6, -0.6, -31.9, -23.6, -69.3, -92.7],
        connector={
            "mode": "between",
            "line": {"width": 2, "color": "rgb(0, 0, 0)", "dash": "solid"},
        },
    )
)


fig.update_layout(title="Национальные счета, РФ, 2018, млрд.руб.")

fig.write_html("sna-ru.html", auto_open=True)

fig.show()
