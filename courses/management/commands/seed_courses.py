# BaseCommand: Classe base para criar comandos personalizados no Django.
# Ao herdar dessa classe, pode ser criado comandos que são executados
# pelo manage.py no terminal.
from django.core.management.base import BaseCommand

from courses.models import Course


class Command(BaseCommand):
    help = "Seed para cadastrar registro na tabela courses."

    def handle(self, *args, **options):
        description = "<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus imperdiet nisi eu urna faucibus, non viverra elit faucibus. Integer vehicula, neque a blandit tincidunt, lacus mi posuere ipsum, vitae pharetra augue erat id lacus. Curabitur accumsan nisl nec nisi tincidunt, nec volutpat mauris fermentum. Fusce non magna id urna consequat pretium. Cras luctus arcu in turpis interdum, a bibendum nulla fringilla.</p><p><strong>O que voc&ecirc; aprender&aacute; neste curso?</strong></p><ul><li><strong>Fundamentos de Python</strong>: Quisque consequat lacus vel metus posuere, sit amet tincidunt felis vehicula. Integer sagittis enim nec mi venenatis vehicula.</li><li><strong>Introdu&ccedil;&atilde;o ao Django</strong>: Vestibulum ac tortor aliquet, eleifend lectus nec, sollicitudin ligula. Suspendisse ultricies purus non nisl suscipit, ut vehicula ipsum sodales.</li><li><strong>Cria&ccedil;&atilde;o de Aplica&ccedil;&otilde;es Web</strong>: Nam varius elit ut urna aliquet, in viverra turpis molestie.</li><li><strong>Modelos e Banco de Dados</strong>: Sed dictum metus nec nisi convallis, sed ultricies lorem luctus.</li><li><strong>Autentica&ccedil;&atilde;o de Usu&aacute;rios</strong>: Proin eget felis id lectus efficitur feugiat vitae at quam.</li><li><strong>API com Django REST Framework</strong>: Morbi a nulla id ex porttitor tincidunt et ac est.</li><li><strong>Desenvolvimento Frontend com Django Templates</strong>: Curabitur luctus velit in tellus iaculis, vel sodales ipsum vehicula.</li></ul><p><strong>Por que escolher este curso?</strong></p><ul><li>Donec faucibus mi sit amet arcu pharetra, quis luctus arcu iaculis.</li><li>Integer consequat justo a felis dictum, at blandit orci convallis.</li><li>Fusce ornare turpis nec urna molestie, nec tincidunt eros faucibus.</li><li>Sed euismod lorem a turpis fermentum, vitae vehicula nisi malesuada.</li></ul><p><strong>Roteiro do Curso:</strong></p><ol><li><strong>M&oacute;dulo 1</strong> &ndash; Lorem ipsum dolor sit amet, consectetur adipiscing elit.</li><li><strong>M&oacute;dulo 2</strong> &ndash; Integer ut odio in mauris accumsan malesuada.</li><li><strong>M&oacute;dulo 3</strong> &ndash; Aenean convallis nisl ut sapien varius, vitae consectetur sapien viverra.</li><li><strong>M&oacute;dulo 4</strong> &ndash; Phasellus interdum augue et est vestibulum, nec sodales arcu luctus.</li></ol><p><strong>Benef&iacute;cios para voc&ecirc;:</strong></p><ul><li>Cras nec felis in turpis facilisis vulputate.</li><li>Praesent vitae velit et elit vehicula convallis.</li><li>Nulla facilisi: acesse o curso a qualquer momento e de qualquer lugar!</li></ul><p>Suspendisse potenti. Fusce vel turpis ut libero eleifend tincidunt. <strong>Inscreva-se agora e comece a dominar Python e Django hoje mesmo!</strong></p><p><em>Oferta v&aacute;lida por tempo limitado!</em></p>"  # noqa E501

        # Criar a lista de cursos com os dados a serem cadastrados
        courses = [
            {
                "name": "Curso de Python",
                "original_price": 497.43,
                "discounted_price": 347.61,
                "description": description,
            },
            {
                "name": "Curso de Django",
                "original_price": 597.43,
                "discounted_price": 447.61,
                "description": description,
            },
            {
                "name": "Curso de Python e Django",
                "original_price": 997.43,
                "discounted_price": 847.61,
                "description": description,
            },
        ]

        # Iterar sobre a lista de cursos
        for course_data in courses:
            # Atualiza o registro existente ou cria um novo com base
            # no nome do curso
            Course.objects.update_or_create(
                name=course_data["name"],  # Critério de busca: nome do curso
                defaults=course_data,  # Valores padrão para criar ou atualizar
            )

        # Exibe uma mensagem no terminal indicando o sucesso da operação
        self.stdout.write(
            self.style.SUCCESS("Cursos adicionados com sucesso!")
        )
