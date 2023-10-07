var vg_1 = "bubble_map.vg.json";
vegaEmbed("#bubble_map", vg_1)
  .then(function (result) {
    result.view;
  })
  .catch(console.error);
