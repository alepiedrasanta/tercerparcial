<template>
     <center>
    <div>
    <h1>Actualizar Computadora</h1>
    <br>
    <h2>Codigo de equipo: {{id=$route.params.id}} </h2>
    <form  action="" @submit.prevent="mounted()">
      <div class="card-body">
         <div class="card-subtitle mb-2 text-muted">
        <h3>Marca</h3>
        <input v-model="marca" type="text" class="form-control">
        <h3>Detalles</h3>
        <input v-model="detalles" type="text" class="form-control">
        <h3>Precio</h3>
        <input v-model="precio" type="text" class="form-control">
        <br>
        <button type="submit" class="btn btn-outline-info" name="button">Actualizar</button>
        </div>
      </div>
    </form>
  </div>
  </center>
</template>
 
<script>
  import axios from 'axios'
  export default{
    name: 'Computadora',
    data(){
      return {
        marca: this.$route.params.marca,
        detalles: this.$route.params.detalles,
        precio: this.$route.params.precio,
        id: '',
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
  actualizarcomputadora(input:{id:"`+this.id+`", marca:"`+this.marca+`", detalles:"`+this.detalles+`",precio:"`+this.precio+`"}){
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
