<template>
 
  <center>
    <div>
    <h1>Agregar nueva computadora</h1>
    <br>
    <form  action="" @submit.prevent="mounted()">
      <div class="card-body">
         <div class="card-subtitle mb-2 text-muted">
        <h3>Marca</h3>
        <input v-model="marca" marca="" type="text" class="form-control">
        <h3>Detalles</h3>
        <input v-model="detalles" detalles="" type="text" class="form-control">
        <h3>Precio</h3>
        <input v-model="precio" precio="" type="text" class="form-control">
        <br>
        <button type="submit" class="btn btn-outline-info" name="button">Crear</button>
        </div>
      </div>
    </form>
  </div>
  </center>
 
</template>
 
<script>
  import axios from 'axios'
  export default{
    name: 'Computadoras',
    data(){
      return {
        marca: '',
        detalles: '',
        precio: '',
        directory: []
      }
    },
    methods: {
    async mounted () {
  try {
        var result = await axios({
          method: 'POST',
          url: 'http://localhost:8000/graphql',
          data: {
            query: `
            mutation{
  crearcomputadora(input:{marca:"`+this.marca+`",detalles:"`+this.detalles+`",precio:"`+this.precio+`"}){
    computadora{
      id
      marca
      detalles
      precio
    }
  }
}
            `
          }
        })
        this.directory = result.data.data.todascomputadoras
      } catch (error) {
        console.error(error)
      }
    }
  }
}
</script>
