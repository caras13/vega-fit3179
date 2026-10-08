var vis1 = "jsons/map_1_choropleth.json";
vegaEmbed('#vis1', vis1).then(function(result) {
  // Access the Vega view instance (e.g. result.view) if needed
}).catch(console.error);