const principal = {
    template: `<div> <h1>Esta es la página principal, bienvenidos!!!</h1>
        <h3 style="color: blue;">Click sobre la imagen</h3>
        <img style="cursor:pointer;" @click="showInfo()" src="recursos/uni.png">
    </div>`,


    methods:{
        showInfo(){
            alert("Bienvenido tripulante");
        }
    }
}
