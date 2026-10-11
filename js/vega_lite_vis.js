// var vis1 = "jsons/map_1_choropleth.json";
// vegaEmbed('#vis1', vis1).then(function(result) {
//   // Access the Vega view instance (e.g. result.view) if needed
// }).catch(console.error);
var spec1 = "jsons/map_1_choropleth.json";

vegaEmbed('#map_1', spec1, { "actions": false }).then(function(result) {
  console.log("Chart 1 loaded successfully");
}).catch(function(error) {
  console.error(error);
});

var spec2 = "jsons/map_2_symbols.json";

vegaEmbed('#map_2', spec2, { "actions": false }).then(function(result) {
  console.log("Chart 2 loaded successfully");
}).catch(function(error) {
  console.error(error);
});

var specDumbbell = "jsons/chart_2_dumbbell.json";

vegaEmbed('#vis_dumbbell', specDumbbell, { "actions": false }).then(function(result) {
  console.log("Chart 2 Dumbbell Plot loaded successfully");
}).catch(console.error);
// vegaEmbed('#vis1', 'jsons/map_1_choropleth.json');
// vegaEmbed('#vis2', 'jsons/chart_1_dumbbell.json');
// vegaEmbed('#vis3', 'jsons/map_2_symbols.json');
// ... embed all 11+ charts