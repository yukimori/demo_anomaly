(function($){
    var labelLength = 30;
    var data = {
    labels: _.range(1,labelLength),
    datasets: [
        {
            label: "My First dataset",
            fillColor: "rgba(220,220,220,0.2)",
            strokeColor: "rgba(220,220,220,1)",
            pointColor: "rgba(220,220,220,1)",
            pointStrokeColor: "#fff",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(220,220,220,1)",
            data: _.range(1,labelLength)
        },
        {
            label: "My Second dataset",
            fillColor: "rgba(151,187,205,0.2)",
            strokeColor: "rgba(151,187,205,1)",
            pointColor: "rgba(151,187,205,1)",
            pointStrokeColor: "#fff",
            pointHighlightFill: "#fff",
            pointHighlightStroke: "rgba(151,187,205,1)",
            data: _.range(1,labelLength)
        }
    ]
	};
    $(function(){
	console.log("onload");
	var ctx = document.getElementById("myChart").getContext("2d");
	var myNewChart = new Chart(ctx).Line(data,{datasetFill: false});
        var dataset0 = myNewChart.datasets[0];
	var timer = setInterval(function(){
            for(i=0; i < dataset0.points.length; i+=1){
                dataset0.points[i].value = (i+1 != dataset0.points.length) ? 
                    dataset0.points[i+1].value: _.random(0,100);;
            }
	    myNewChart.update();
	    },500);
	})
    
})(jQuery);
