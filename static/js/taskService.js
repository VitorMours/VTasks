class TaskService{
    static api = "localhost:5000"
    static config = {
        headers: {
            "Content-Type": "application/json"
        },
        credentials: include
    }


    /**
     * Metodo Responsavel por atualizar o status de uma determinada tarefa que deve existir, 
     * para que possa ser atualizada, mudando o seu status de maneira e valor booleano
     * @param {Task} Task - qual task tera seu valor mudado, e sera feito de forma a pegar o que ja esta sendo mostrado, e mudar
     * nao possibilitando insercao de valor de maneira externa.
     */
    async changeTaskStatus(json){
        const response = await fetch("/api/", {
            method: "PUT",
            ...config
        })
        console.log(response);
    }

}