# Odoo Academy

#### Criação do Módulo Odoo Academy

A aplicação tera funcionalidades como a criação de cursos, alocação de aulas dentro desses cursos, estas que terão alunos e professores associados,terão data de inicio e término, vagas disponíveis e duração.

##### Estrutura básica do módulo:

```bash
├── __init__.py
├── __openerp__.py
├── models
│   ├── __init__.py
│   ├── courses.py
│   ├── partners.py
│   └── session.py
└── views
    ├── courses_view.xml
    ├── partners_view.xml
    └── session_view.xml
```
`__init__.py`: Este arquivo permite transformar a pasta em que esta alocado em módulo(estrutura que irá agrupar os arquivos presentes, facilitando na imporatação)

```python
#Arquivo __init__ localizado em models
from . import courses
from . import partners
from . import session
```

`__openerp__.py`: Este arquivo permite funciona como manifesto do módulo, nele estão informações sobre a aplicação e especificações de dependências e views.

```python
{
    'name': 'Nome Módulo'
    'version': 'Versão Módulo'
    'summary': 'Sumário Módulo'
    'description': 'Descrição'
    'category': 'Categoria'
    'author': 'Autor da Aplicação'
    'website': 'Website'
    'license': 'licença(AGPL-3)'
    'depends':['dependencia.modulo1', 'dependencia.modulo12]
    'data':['views/view1_view1.xml',
            'views/view1_view2.xml],
}
```

#### Criação das Models Session, Courses e Partners

-Dentro das models serão especificados os campos a serem exibidos nas views, especificação de dependencias nesses campos, os comportamentos/métodos executados, bem como seus gatilhos.

##### Modelo básico de uma model:

```python
from openerp import fields, models, api

Class Model1(models.Model):

    _name = 'modulo.nomeclasse'
    abool = fields.Boolean()
    achar = fields.Char()
    atext = fields.Text()
    anhtml = fields.Html()
    anint = fields.Integer()
    afloat = fields.Float()
    adate = fields.Date()
    abin = fields.Binary()
    aselection = fields.Selection([('valorASerGuardado1', 'TextoExibido1'),('valorASerGuardado2', 'TextoExibido2')])
    //Geralmente o campo abaixo fica em outra model, levando em consideração que se queira fazer relação entre models
    arel_id = fields.Many2one(comodel_name='res_partner')
    //O atributo 'rel_id' trata-se do campo Many2one a qual se quer relacionar
    arel_ids = fields.One2many(comodel_name='res_partner', inverse_name = 'rel_id')
    
    //O método abaixo é acionado quando há mudanças em achar 
    @api.onchange(achar)
    def _faz_alguma_coisa(self)
        ...
        pass
        
    def _faz_outra_coisa(self)
        ...
        pass
```
Os campos mostrados acima são opções que podem ser implementadas nos formulários que serão montados. dentro desses campos há diversas opções de __atributos__, que podem customizar sua aparência ou relaciona-los a gatilhos(openerp.api). 

```python
    name = fields.Char(
        string="Name",                   
        compute="_compute_name_custom",  
        store=True,                      
        select=True,                     
        readonly=True,                   
        inverse="_write_name"            
        required=True,                   
        translate=True,                  
        help='blabla',                   
        company_dependent=True,          
        search='_search_function'        
    )
```
Abaixo á uma lista dos que podem ser implementados.

__*string*__: string de exibição do campo.<br>
__*compute*__: transforma o campo em questão em um campo computed, o associando a uma função que determinará seu valor dinamicamente.<br>
__*store*__: Utilizado juntamente com o atributo *compute*, tem valor booleano, quando *True*, salva o campo na tabela da model em questão.
__*select*__: Força um index no campo.<br>
__*readonly*__: o campo não poderá ser alterado.<br>
__*inverse*__: funciona como um gatilho, associa-se esse atributo a uma função, que será chamada sempre que houver atualizações.<br>
__*required*__: torna o campo obrigatório, caso True.<br>
__*translate*__: Ativa o Tranlation(tradutor).<br>
__*help*__: cria um *help* para o campo, uma espécie de breve descrição.<br>
__*search*__: atribui uma função de pesquisa customizada, geralmente utilizada em conjunto com o atributo *compute*.<br>
__*company_dependent*__: Transforma o campo dependente a compania de registro, usuários cadastrados em diferentes companias, poderão ver valores diferentes para a mesma coluna.<br>
__*default*__: Define um valor padrão para o campo.<br>
__*related*__: torna o campo diretamente relacionado a alterações em outra model.<br>

#### Criação das Views de Session, Courses e Partners

-Dentro das views serão alocados os campos criados nas models, e por meio de tags, customizar sua exibição/posicionamento.

##### Estrutura básica de uma view

```xml
<openerp>
    <data>
    
        <!--O menu abaixo será exibido na barra superior-->
        <menuitem id="id_novomenu" name="Nome Módulo" sequence="450"/>
    
        <!--O atributo model classifica o tipo -->
        <!--de record criado, no caso abaixo ir.ui.view,-->
        <!--utilizado para views que exibirão estruturas-->
        <!--como form, tree, kanban, graph dentre outros-->
        
        <record model="ir.ui.view" id="view_nomemodulo_nomemodel_form">
            <field name="name">Nome Record</field>
            <field name="model">Nome da Model</field>
            <field name="arch" type="xml">

                <!--Neste espaço colocamos os campos criados-->
                <!--na model, e escolhemos o tipo de exibição-->
                <!--(tag de kanban, tree, form e etc), há-->
                <!--limitações de campos e atributos dependendo-->
                <!--do tipo de exibição escolhido, neste caso-->
                <!--exibiremos o tipo form(Exibira Formulario-->
                
                <form>
                    
                    <!--A tag 'header' agrupa elementos no CABEÇALHO do formulário-->
                    <header>
                        <!--O 'widget' statusbar transforma o campo do tipo select em uma status bar(também há um widget que o exibe em formato radio)-->
                        <field name="aselection" widget="statusbar"/>
                    </header>
                
                    <!--A tag 'sheet' agrupa elementos no CORPO do formulário-->
                    <sheet>
                    
                        <!--A tag 'group' agrupa os campos-->
                        <group>
                            <field name="abool"/>
                            <field name="achar"/>
                            <field name="atext"/>
                            <field name="anint"/>
                        </group>
                        
                        <button string="Faz Algo" type="object" name="_faz_outra_coisa"/>
                        
                        <!--A tag notebook cria exibição em abas, que são identificadas pela tag 'page'-->
                        <notebook>
                            <page string="String Pagina">
                                <field name="arel_ids"/>
                            </page>
                        </notebook>
                    </sheet>
                </form>

            </field>
        </record>
        
        <record model="ir.ui.view" id="view_nomemodulo_nomemodel_tree">
            <field name="name">Nome Record</field>
            <field name="model">Nome da Model</field>
            <field name="arch" type="xml">
            
                <!--O tag tree, especificada abaixo, determina-->
                <!--que o record em questão, exibira os campos em-->
                <!--formato de lista-->
                <tree string="Session">
                    <field name="achar"/>
                    <field name="aint"/>
                </tree>
                
            </field>
        </record>
        
        <!--Os menus abaixo serão exibidos na barra lateral-->
        <menuitem id="id_submenu" name="Titulo Menu"
                  parent="id_novomenu" sequence="1"/>
        
        <!--O atributo 'action' chama o record com o id especificado-->
        <menuitem id="submenu_model1" name="Model1"
                  parent="id_submenu"
                  action="action_modulo_model" sequence="1"/>
                  
        <record id="action_nomemodulo_nomemodel" model="ir.actions.act_window">
            <field name="name">Nome Record</field>
            <field name="type">ir.actions.act_window</field>
            <field name="res_model">Nome da Model</field>
            <field name="view_mode">tree,form</field>
        </record>

    </data>
</openerp>
```

## Módulo Locadora

Construa as models Categoria, Filme, OperacaoUnit, OperacaoConj e Cliente

* **Cliente:**
    * filme_ids - many2many
    * operacaoconj_ids - one2many
    * valor_gasto - float(será um campo *compute*)
* **Categoria:**
    * nome - char
    * filme_ids - many2many
* **Filme:**
    * titulo - char
    * categoria_ids - many2many
    * valor - float
    * descrição - text
    * data - date
    * quantidade - int
    * autor - char
* **OperacaoUnit:**
    * operacaounit_id - many2one
    * tipo - select [venda, aluguel]
    * preco - float(será um campo *compute*)
    * filme_ids - many2many
    * status - select [indisponível, em espera, disponível, atrasado](será um campo *compute*)
    * dataOperacao - date
    * dataEntrega - date(o campo em questão só fica aberto a escrita quando tipo(OperacaoUnit) é aluguel)
* **OperacaoConj:**
    * operacaounit_ids - one2many
    * cliente_id - many2one
    * valor - float(será um campo *compute*)
    
##### Observações sobre alguns campos:
-O campo  valor em OperacaoConj deve ser a soma de todos os preços definidos em instancias associadas de OperacaoUnit, será necessário utilizar o módulo api, mais especificamente o decorator api.depends(*mais detalhes sobre os decorator de api na [documentação](https://www.odoo.com/documentation/8.0/reference/orm.html#module-openerp.api)

-O campo  valor_gasto em Cliente deve ser a soma de todos os valores definidos em instancias associadas de OperacaoConj

-Assim como foi dito acima, o campo preco(OperacaoUnit) é dependente direto de tipo(OperacaoUnit), dataEntrega(OperacaoUnit), e data(Filme), será necessário utilizar o módulo api, mais especificamente o decorator api.depends(*mais detalhes sobre os decorator de api na [documentação](https://www.odoo.com/documentation/8.0/reference/orm.html#module-openerp.api)*)
        
*Para mais detalhes de como manusear campos relacionais (one2many, many2one, many2many, visite a [documentação oficial](https://www.odoo.com/documentation/8.0/reference/orm.html#relational-fields), ou observe um [caso de uso](https://www.odoo.com/documentation/8.0/howtos/backend.html) fornecido pelo odoo com exemplos de uso para cada campo relacional).*

#### Detalhes do funcionamento do módulo

*  Ao salvar uma operaçãoUnit com tipo aluguel(alugar um filme), definir o preço como R$4,00 caso for lançamento(com campo data de no maximo 3 meses de diferença da data atual), senão definir preço como R$2,00.

* O prazo de entrega do filme é de 2 dias, caso haja atraso, cobrar juros simples de 50% do valor definido em preço(OperacaoUnit) por dia de atraso.

* Caso a operação seja do tipo venda, cobrar no filme um valor de 30% a mais do seu valor(Filme), e logicamente decrescer a quantidade do estoque.

* Ao criar uma OperacaoUnit o campo dataOperacao recebe a data atual.

* Ao alugar filme, este fica temporariamente fora de estoque, até ser devolvido(decrescido do estoque)

* Campo status deve ser um workflow com as opções que foram descritas na criação da model, os status a seguir terão os seguintes botões para edição de status.
    * Alugar - somente em status 'Disponível'
    * Vender - somente em status 'Disponível'
    * Concluir - somente em status 'Em espera' ou 'Atrasado'

* A definição do status exibido por OperacaoUnit depende de algumas condições.
    * Indisponível - quando não há cópias do filme em estoque, ou alugadas.
    * Em espera - quando não há cópias em estoque porém existe cópias alugadas dentro do prazo de entrega, neste caso deve ser exibida a data de entrega da cópia do filme que foi alugada com data de entrega mais proxima da data atual(dentro do campo dataEntrega).
    * Atrasado - quando não há cópias em estoque porém existem cópias alugadas dentro fora do prazo de entrega, neste caso esse status é exclusivo de OperacaoUnit que ainda estão a ser feitas(que ainda não foram criadas).
    * Disponível - quando há cópias em estoque, diponíveis para operações(venda ou aluguel)
    
*Na documentação oficial há um exemplo de como criar um workflow completo segue o [link](https://www.odoo.com/documentation/8.0/howtos/backend.html#workflows))*
