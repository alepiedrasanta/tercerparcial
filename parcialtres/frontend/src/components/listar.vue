<template>
<center>
  <a :href="`/computadora/crear/`" class="btn btn-outline-success">Crear</a>
<div class="card text-center" v-for="input in directory.edges" :key="input.id">
  <div class="card-body">
    <h3 class="card-subtitle mb-2 text-muted">{{ input.node.marca }}</h3>
  </div>
  <div class="card-body">
    <h3 class="card-subtitle mb-2 text-muted">Detalles</h3> 
    <p class="card-text">{{ input.node.detalles }}</p>
 </div>
  <div class="card-body">
    <h3 class="card-subtitle mb-2 text-muted">Precio</h3>
    <p class="card-text">{{ input.node.precio }}</p>
  </div>
  <div class="card-footer text-muted">
      <td type="button" class="btn btn-outline-info"><a :href="`/computadora/actualizar/${input.node.id}/${input.node.marca}/${input.node.detalles}/${input.node.precio}`">Actualizar</a></td>
  </div>
</div>
</center>
</template>
 
<script>
  import axios from 'axios'
  export default{
name: 'Computadora',
    data(){
      return {
    directory: []
      }
    },
    async mounted () {
    try {
  var result = await axios({
    method: 'POST',
    url: 'http://localhost:8000/graphql',
    data: {
      query: `
      {
          todascomputadoras {
                    edges {
                    node {
                        id
                        marca
                        detalles
                        precio
                    }
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
</script>
 
