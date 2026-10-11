// Chart 1: State Choropleth Map
vegaEmbed('#map_1', 'jsons/map_1_choropleth.json', { "actions": false })
  .then(() => console.log("Chart 1 loaded"))
  .catch(console.error);

// Chart 2: Metro vs Regional Dumbbell
vegaEmbed('#vis_dumbbell', 'jsons/chart_2_dumbbell.json', { "actions": false })
  .then(() => console.log("Chart 2 loaded"))
  .catch(console.error);

// Chart 3: NAPLAN Grouped Bar
vegaEmbed('#chart_3', 'jsons/chart_3_grouped_bar.json', { "actions": false })
  .then(() => console.log("Chart 3 loaded"))
  .catch(console.error);

// Chart 4: University Proportional Symbol Map
vegaEmbed('#map_2', 'jsons/map_2_symbols.json', { "actions": false })
  .then(() => console.log("Chart 4 loaded"))
  .catch(console.error);

// Chart 5: Low SES vs High SES Dumbbell
vegaEmbed('#chart_5', 'jsons/chart_5_dumbbell.json', { "actions": false })
  .then(() => console.log("Chart 5 loaded"))
  .catch(console.error);