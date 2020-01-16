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
            x[1]
            for x in [
                ["Выпуск", "Output (X)"],
                ["Импорт", "Import (IM)"],
                ["Статистическое расхождение", "Statistical discrepancy"],
                ["Экспорт", "Export (EX)"],
                ["Инвестиции", "Investment (I)"],
                ["Конечное потребление", "Final consumption (C)"],
                ["Промежуточное потребление", "Intermediate consumption (AX)"],
            ]
        ],
        x=[196.6, 21.6, -0.6, -31.9, -23.6, -69.3, -92.7],
        connector={
            "mode": "between",
            "line": {"width": 2, "color": "rgb(0, 0, 0)", "dash": "solid"},
        },
    )
)

# "Национальные счета, РФ, 2018, млрд.руб."

fig.update_layout(title="Goods and services account (Russia, 2018, trn rub)")

fig.write_html("handout/res_use.html", auto_open=True)

fig.show()
