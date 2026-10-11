// var vis1 = "jsons/map_1_choropleth.json";
// vegaEmbed('#vis1', vis1).then(function(result) {
//   // Access the Vega view instance (e.g. result.view) if needed
// }).catch(console.error);

vegaEmbed('#vis1', 'jsons/map_1_choropleth.json');
vegaEmbed('#vis2', 'jsons/chart_1_dumbbell.json');
vegaEmbed('#vis3', 'jsons/map_2_symbols.json');
// ... embed all 11+ charts