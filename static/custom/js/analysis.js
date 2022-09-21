let tab_tot = document.querySelector("div.tab-tot");
let tab_detail = document.querySelector("div.tab-detail");

let detail_review = document.querySelector("div.detail-review");
let general_review = document.querySelector("div.general-review");


tab_detail.addEventListener("click",function(e){
    e.stopPropagation();
    tab_tot.classList.remove("select-box")
    tab_detail.classList.add("select-box")
    detail_review.classList.remove("not-display")
    general_review.classList.add("not-display")
})

tab_tot.addEventListener("click",function(e){
    e.stopPropagation();
    tab_detail.classList.remove("select-box")
    tab_tot.classList.add("select-box")
    general_review.classList.remove("not-display")
    detail_review.classList.add("not-display")
})

var tot_score=document.querySelector("span.score").innerHTML;

var gauge_options = {
    series: [tot_score],
    chart: {
    type: 'radialBar',
    toolbar: {
      show: false
    }
  },
  colors:["#d12ee5"],
  plotOptions: {
    radialBar: {
      startAngle: -135,
      endAngle: 225,
       hollow: {
        margin: 0,
        size: '70%',
        background: '#fff',
        image: undefined,
        imageOffsetX: 0,
        imageOffsetY: 0,
        position: 'front',
        dropShadow: {
          enabled: true,
          top: 3,
          left: 0,
          blur: 4,
          opacity: 0.24
        }
      },
      track: {
        background: '#fff',
        strokeWidth: '67%',
        margin: 0, // margin is in pixels
        dropShadow: {
          enabled: true,
          top: -3,
          left: 0,
          blur: 4,
          opacity: 0.35
        }
      },
  
      dataLabels: {
        show: true,
        name: {
          offsetY: -10,
          show: true,
          color: '#888',
          fontSize: '17px'
        },
        value: {
          formatter: function(val) {
            return parseInt(val);
          },
          color: '#2A2A2A',
          fontSize: '36px',
          show: true,
        }
      }
    }
  },
  fill: {
    type: 'gradient',
    gradient: {
      shade: 'dark',
      type: 'horizontal',
      shadeIntensity: 0.5,
      gradientToColors: ['#a031f1'],
      inverseColors: true,
      opacityFrom: 1,
      opacityTo: 1,
      stops: [0, 100]
    }
  },
  stroke: {
    lineCap: 'round'
  },
  labels: ['Score'],
  };

  var gauge_chart = new ApexCharts(document.querySelector("div.tot-score"), gauge_options);
  gauge_chart.render();



  var rose_options = {
    series: [100, 50, 70, 50, 70,90,0,0,0,0,0,0],
    // series: [100, 50, 70, 50, 70,90],
    chart: {
    type: 'polarArea',
    width:"60%",
  },
  // labels: ['깜빡임', '머리 움직임',"표정", '말 빠르기', '목소리 톤', '추임새'],
  labels: ['깜빡임', '머리 움직임',"표정", '말 빠르기', '답변 시간', '추임새',"x","X","x","x","x"],
  fill: {
    // colors:["#884ae5","#9a26f0","#a830ee","#ba23e8","#cf22e4"],
    colors:["#cf22e4","#ba23e8","#a830ee","#9a26f0","#884ae5","#704de7"],
    opacity: 1
  },
  stroke: {
    
    width: 0},
  yaxis: {
    show: false
  },
  legend: {
    show: false
  },
  plotOptions: {
    polarArea: {
      rings: {
        strokeWidth: 0
      },
      spokes: {
        strokeWidth: 0
      },

    },  

  },
  theme: {
    mode:"light",
    palette: "palette10"
  }
  };

  var rose_chart = new ApexCharts(document.querySelector("div.rosechart"), rose_options);
  rose_chart.render();