from rh.classes.Departamento import Departamento
from datetime import date, timedelta


class TestDepartamento:
    def test_class_declared(self):
        objeto = Departamento('Time PDI ', 'Evandro Dametto', 7, 3, 2021)
        assert isinstance(objeto, Departamento)

    def test_instanciar(self):
        objeto = Departamento('Time PDI ', 'Evandro Dametto', 7, 3, 2021)
        assert objeto.nome_setor == 'Time PDI '
        assert objeto.responsavel == 'Evandro Dametto'

    def test_str_repr(self):
        objeto = Departamento('Time PDI ', 'Evandro Dametto', 7, 3, 2021)
        assert str(objeto) == 'Time PDI '
        assert repr(objeto) == 'Departamento = Time PDI '

    def test_setters(self):
        objeto = Departamento('Curadoria', 'Ana', 14, 2, 2020)
        assert objeto.nome_setor == 'Curadoria'
        objeto.nome_setor = 'ETL'
        assert objeto.nome_setor == 'ETL'

    def test_properties(self):
        objeto = Departamento('Time PDI ', 'Evandro Dametto', 7, 3, 2021)
        assert objeto.nome_setor == 'Time PDI '

    def test_responsavel(self):
        departamento = Departamento('Time PDI ', 'José da Silva', 1, 1, 1990)
        assert departamento.responsavel == 'José da Silva'

    def test_responsavel_substituido(self):
        departamento = Departamento('Time PDI ', 'José da Silva', 1, 1, 1990)
        assert departamento.responsavel is not None
        assert departamento.responsavel == 'José da Silva'
        departamento.informar_responsavel('João Oliveira', 1, 1, 1990)
        assert departamento.responsavel == 'João Oliveira'

    def test_add_colaborador(self):
        departamento = Departamento('Time PDI ', 'José da Silva', 1, 1, 1990)
        departamento.add_colaborador('João Oliveira', 18, 3, 1992)
        departamento.add_colaborador('Pedro Mendonça', 18, 4, 1993)
        assert len(departamento.colaboradores) == 2

    def test_verificar_aniversariantes(self):
        retorno = [('João Oliveira', '1992-03-28', 'José da Silva', 'Time PDI '), 
                   ('Luis Fernando', '2000-03-28', 'José da Silva', 'Time PDI ')]
        dt1 = date.today() - timedelta(days=4)
        hoje = date.today()
        depto = Departamento('Time PDI ', 'José da Silva', dt1.day, dt1.month, 1990)
        depto.add_colaborador('João Oliveira', hoje.day, hoje.month, 1992)
        depto.add_colaborador('Pedro Mendonça', dt1.day, dt1.month, 1993)
        depto.add_colaborador('Luis Fernando', hoje.day, hoje.month, 2000)
        depto.add_colaborador('Maurício Souza', dt1.day, dt1.month, 1085)
        aniversariantes = depto.verificar_aniversariantes()
        assert aniversariantes == retorno
        assert len(aniversariantes) == 2
        assert len(aniversariantes[0]) == 4
        assert type(aniversariantes[0]) == tuple
        assert type(aniversariantes) == list
