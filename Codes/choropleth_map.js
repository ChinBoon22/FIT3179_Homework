var vg_1 = "choropleth_map.vg.json";
vegaEmbed("#choropleth_map", vg_1)
  .then(function (result) {
    // Access the Vega view instance(https://vega.github.io/vega/docs/api/view/) as result.view
    result.view;
  })
  .catch(console.error);
