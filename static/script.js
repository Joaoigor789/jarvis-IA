
    const scene = new THREE.Scene();

    const camera = new THREE.PerspectiveCamera(
        75,
        window.innerWidth / window.innerHeight,
        0.1,
        1000
    );

    const renderer = new THREE.WebGLRenderer({
        canvas: document.getElementById("bg")
    });

    renderer.setSize(window.innerWidth, window.innerHeight);

    const geometry = new THREE.TorusGeometry(10, 3, 16, 100);
    const material = new THREE.MeshBasicMaterial({
        color: 0x00ffff,
        wireframe: true
    });

    const torus = new THREE.Mesh(geometry, material);
    scene.add(torus);

    camera.position.z = 30;

    function animate() {
        requestAnimationFrame(animate);

        torus.rotation.x += 0.01;
        torus.rotation.y += 0.01;

        renderer.render(scene, camera);
    }
    animate();

    
    const ctx1 = document.getElementById('chart').getContext('2d');

    const data1 = {
        labels: ["IA", "Cyber", "Web", "Finance", "Space"],
        datasets: [{
            label: "Dados em tempo real",
            data: [12, 19, 8, 15, 10],
            borderWidth: 2
        }]
    };

    const chart1 = new Chart(ctx1, {
        type: 'line',
        data: data1
    });

    
    const ctx2 = document.getElementById('chart2').getContext('2d');

    const chart2 = new Chart(ctx2, {
        type: 'bar',
        data: {
            labels: ["CPU", "RAM", "NET", "GPU"],
            datasets: [{
                label: "Sistema",
                data: [30, 50, 20, 40]
            }]
        }
    });

    setInterval(() => {
        data1.datasets[0].data = data1.datasets[0].data.map(
            () => Math.floor(Math.random() * 20)
        );
        chart1.update();

        chart2.data.datasets[0].data = chart2.data.datasets[0].data.map(
            () => Math.floor(Math.random() * 100)
        );
        chart2.update();
    }, 2000);

    
    const topics = [
        "Inteligência Artificial",
        "Cibersegurança",
        "Mercado Financeiro",
        "Tecnologia 2026",
        "Programação Web",
        "Carros Autônomos",
        "Espaço",
        "Blockchain",
        "Startups",
        "Robótica"
    ];

    const container = document.getElementById("topics");

    let i = 0;

    function showTopic() {
        if (i < topics.length) {
            const p = document.createElement("p");
            p.classList.add("scan-line");
            p.innerText = "Escaneando: " + topics[i];
            container.appendChild(p);

            i++;
            setTimeout(showTopic, 1000);
        }
    }

    showTopic();

    
    const logs = document.getElementById("logs");

    setInterval(() => {
        const msg = document.createElement("p");
        msg.innerText = "Processando dados... " + Math.random().toFixed(4);
        logs.appendChild(msg);

        logs.scrollTop = logs.scrollHeight;
    }, 1500);