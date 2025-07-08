- [x] Terminar servico de autenticacao do signin - Finished in 16-06-2025
    - [x] Terminar o servico de Signin, com hash de senhas, 
    - [ ] Logar o usuario automaticamente dentro da sessao depois de fazer o login ou sign de maneira coreta dentro da paltaforma
    - [x] Fazer uma verififcacao do banco de dados antes de salvar o usuario, de forma que facilite a forma de verfiicar se o usuario ja existe, ou se tem algum problema dele ser cadastrado
    
- [ ] Crair scrpits javascript para receber os dados provenientes do flask 
- [x] Estudar a diferenca entre PWA e SPA
- [ ] Estudarsobre a possibilidade de colocar essa aplicação como um PWA


# 05/07/2025

- [ ] Create the security for the pagesto user to be logged to access 



# 07/07/2025
Foi feito todo o esquema de criação, e de desenvolvimento das tasks que estão linkadas por meio de chave estrangeira com usuário, fazendo com que seja impossível criar uma task, sem que tenha um usuário cadastrado dentro da base de dados que 
esteja em vias de fato conectado com essa task.
Com isso, agora torna-se apenas necessário fazer o desenvolvimento do macro necessário para que sejam mostradas as tasks 
dentro da interface para o usuário, de forma que são aplicados filtros dentro dessa interface, em que dividimos as tasks
em todas, as tasks ativas, e as tasks que já foram concluída. Com isso, temos a necessidade de codificar ainda o desenvolvimento das possibilidades de edição e de deleção de alguma task por parte do usuário


# 08/07/2025
Atualmente a funcionalidade de criar e mostrar as tasks esta correta, entretanto precisa-se fazer com que ao criar uma nova task, ela seja automaticamente enviada
e mostrada dentro da interface, para que possamos ter mais interatividade e fique mais facil para o usuario. Estou pensando em usar o localStorage do javascript apra quando tiver uma task dentro da interface criada que ainda nao foi enviada para o banco de dados, ela ficar salva e mostrada, de forma que fique mais facil de trabalhar com ela enquanto nao consigo dar auto-browser-referesh dentro da itnerface por mei odo backend