/**
 * Responsable class for creating the tasks and managing as an entity for the front-end
*/
class Task{
  /**
   * Construtor de uma Task, de forma que possa ser manejada como uma entidade dentro do front-end 
   *  @param {string} taskConclusion - Nome da tarefa 
   *  @param {uuid} id - Nome da tarefa 
   *  @param {uuid} user_id - Nome da tarefa 
   *  @param {string} taskName - Nome da tarefa 
   *  @param {string} taskDescription - Descrição detalhada da tarefa 
   */
  constructor(taskName, taskDescription){
    this.id = id;
    this.taskConclusion = taskConclusion;
    this.taskName = taskName;
    this.taskDescription = taskDescription;
    this.user_id = user_id;
  }


  /**
   * Get the id value of the task
   * @return {number} id - the identificator of the task
   */
  get id(){
    return this.id;
  }

  /**
   * Get the task name
   * @return {String} name - Get the task name
   */
  get taskName(){
    return this.taskName;
  }

  /**
   * Get the task description
   * @return {String} description - Get the task description
   */
  get taskDescription(){
    return this.taskDescription;
  }

  /**
   * Get the task conclusion
   * @return {String} conclusion - Get the task conclusion
   */
  get taskConclusion(){
    return this.taskConclusion;
  }

  /**
   * Setting the task name
   * @param {String} newName - the new name of the task
   */
  set taskName(newName){
    this.taskName = newName;
  }

  /**
   * Setting the task description
   * @param {String} newDescription - the new description of the task
   */
  set taskDescription(newDescription){
    this.taskDescription = newDescription;
  }
  /**
   * Setting the task conclusion
   * @param {String} newConclusion - the new conclusion status of the task
   */
  set taskConclusion(newConclusion){
    this.taskConclusion = newConclusion;
  }
}