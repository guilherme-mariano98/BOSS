import os
import django

# Set up Django environment
backend_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(backend_dir)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'boss_shopp.settings')
django.setup()

from api.models import Category, Product

def populate_categories():
    categories_data = [
        {'name': 'Moda', 'slug': 'moda', 'description': 'Roupas e acessórios'},
        {'name': 'Eletrônicos', 'slug': 'eletronicos', 'description': 'Dispositivos eletrônicos'},
        {'name': 'Casa', 'slug': 'casa', 'description': 'Produtos para o lar'},
        {'name': 'Games', 'slug': 'games', 'description': 'Jogos e acessórios'},
        {'name': 'Esportes', 'slug': 'esportes', 'description': 'Equipamentos esportivos'},
        {'name': 'Infantil', 'slug': 'infantil', 'description': 'Produtos para crianças'},
        {'name': 'Beleza', 'slug': 'beleza', 'description': 'Produtos de beleza e cuidados pessoais'},
        {'name': 'Livros', 'slug': 'livros', 'description': 'Livros, revistas e e-books'},
        {'name': 'Automotivo', 'slug': 'automotivo', 'description': 'Acessórios e peças para veículos'},
        {'name': 'Pet Shop', 'slug': 'pet-shop', 'description': 'Produtos para animais de estimação'},
        {'name': 'Alimentos', 'slug': 'alimentos', 'description': 'Alimentos e bebidas'},
        {'name': 'Ferramentas', 'slug': 'ferramentas', 'description': 'Ferramentas e equipamentos'},
        {'name': 'Música', 'slug': 'musica', 'description': 'Instrumentos musicais e acessórios'},
        {'name': 'Saúde', 'slug': 'saude', 'description': 'Produtos de saúde e bem-estar'},
        {'name': 'Brinquedos', 'slug': 'brinquedos', 'description': 'Brinquedos e jogos infantis'},
        {'name': 'Papelaria', 'slug': 'papelaria', 'description': 'Material escolar e de escritório'},
    ]
    
    for cat_data in categories_data:
        category, created = Category.objects.get_or_create(
            slug=cat_data['slug'],
            defaults=cat_data
        )
        if created:
            print(f"Created category: {category.name}")
        else:
            print(f"Category already exists: {category.name}")

def populate_products():
    # Get categories
    moda = Category.objects.get(slug='moda')
    eletronicos = Category.objects.get(slug='eletronicos')
    casa = Category.objects.get(slug='casa')
    games = Category.objects.get(slug='games')
    esportes = Category.objects.get(slug='esportes')
    infantil = Category.objects.get(slug='infantil')
    beleza = Category.objects.get(slug='beleza')
    livros = Category.objects.get(slug='livros')
    automotivo = Category.objects.get(slug='automotivo')
    petshop = Category.objects.get(slug='pet-shop')
    alimentos = Category.objects.get(slug='alimentos')
    ferramentas = Category.objects.get(slug='ferramentas')
    musica = Category.objects.get(slug='musica')
    saude = Category.objects.get(slug='saude')
    brinquedos = Category.objects.get(slug='brinquedos')
    papelaria = Category.objects.get(slug='papelaria')
    
    products_data = [
        # Moda
        {'name': 'Camiseta Básica', 'description': 'Camiseta de algodão 100%', 'price': 39.90, 'category': moda},
        {'name': 'Calça Jeans', 'description': 'Calça jeans masculina', 'price': 89.90, 'category': moda},
        {'name': 'Tênis Esportivo', 'description': 'Tênis para corrida', 'price': 169.90, 'category': moda},
        {'name': 'Boné Estiloso', 'description': 'Boné com proteção UV', 'price': 34.90, 'category': moda},
        {'name': 'Jaqueta Corta Vento', 'description': 'Jaqueta leve e impermeável para atividades ao ar livre', 'price': 129.90, 'category': moda},
        {'name': 'Meias Esportivas', 'description': 'Pacote com 3 pares de meias técnicas antitranspirantes', 'price': 29.90, 'category': moda},
        {'name': 'Relógio Inteligente', 'description': 'Smartwatch com monitoramento de saúde e notificações', 'price': 349.90, 'category': moda},
        {'name': 'Óculos de Sol', 'description': 'Óculos UV400 com armação leve e moderna', 'price': 89.90, 'category': moda},
        
        # Eletrônicos
        {'name': 'Smartphone Premium', 'description': 'Smartphone com câmera de 108MP', 'price': 1760.00, 'category': eletronicos},
        {'name': 'Notebook Ultrafino', 'description': 'Notebook com processador i7', 'price': 2975.00, 'category': eletronicos},
        {'name': 'Fone Bluetooth Sem Fio', 'description': 'Fone com cancelamento de ruído', 'price': 224.90, 'category': eletronicos},
        {'name': 'Smart TV 55"', 'description': 'TV 4K com HDR', 'price': 1750.00, 'category': eletronicos},
        {'name': 'Tablet 10 polegadas', 'description': 'Tablet com processador octa-core e 128GB', 'price': 899.90, 'category': eletronicos},
        {'name': 'Câmera Digital 4K', 'description': 'Câmera com lentes intercambiáveis', 'price': 2199.90, 'category': eletronicos},
        {'name': 'Caixa de Som Bluetooth', 'description': 'Caixa de som portátil com 20W RMS', 'price': 159.90, 'category': eletronicos},
        {'name': 'Carregador Portátil 20000mAh', 'description': 'Carregador rápido com 3 portas USB', 'price': 129.90, 'category': eletronicos},
        
        # Casa
        {'name': 'Sofá Confortável', 'description': 'Sofá de 3 lugares', 'price': 1020.00, 'category': casa},
        {'name': 'Cama Queen Size', 'description': 'Cama com headboard', 'price': 899.90, 'category': casa},
        {'name': 'Jogo de Talheres', 'description': 'Talheres em aço inoxidável', 'price': 159.90, 'category': casa},
        {'name': 'Kit de Lâmpadas LED', 'description': 'Lâmpadas LED econômicas', 'price': 97.40, 'category': casa},
        {'name': 'Conjunto de Panelas', 'description': 'Panelas antiaderentes em alumínio', 'price': 249.90, 'category': casa},
        {'name': 'Tapete Decorativo', 'description': 'Tapete 150x200cm para sala', 'price': 179.90, 'category': casa},
        {'name': 'Mesa de Jantar', 'description': 'Mesa de madeira para 6 pessoas', 'price': 799.90, 'category': casa},
        {'name': 'Cortina Blackout', 'description': 'Cortina térmica e acústica', 'price': 89.90, 'category': casa},
        
        # Games
        {'name': 'Console de Videogame', 'description': 'Console de última geração', 'price': 2250.00, 'category': games},
        {'name': 'Jogo de Tabuleiro', 'description': 'Jogo estratégico para toda família', 'price': 89.90, 'category': games},
        {'name': 'Fone Gamer', 'description': 'Fone com som surround 7.1', 'price': 299.90, 'category': games},
        {'name': 'Teclado Mecânico', 'description': 'Teclado RGB com switches blue', 'price': 319.90, 'category': games},
        {'name': 'Mouse Gamer', 'description': 'Mouse óptico com 16000 DPI', 'price': 189.90, 'category': games},
        {'name': 'Cadeira Gamer', 'description': 'Cadeira ergonômica com ajuste de altura', 'price': 699.90, 'category': games},
        {'name': 'Monitor Gamer 144Hz', 'description': 'Monitor 24 polegadas com taxa de atualização alta', 'price': 999.90, 'category': games},
        {'name': 'Controle Sem Fio', 'description': 'Controle compatível com múltiplos consoles', 'price': 159.90, 'category': games},
        
        # Esportes
        {'name': 'Conjunto de Halteres', 'description': 'Halteres ajustáveis de 5 a 25kg', 'price': 254.90, 'category': esportes},
        {'name': 'Tênis para Corrida', 'description': 'Tênis com amortecimento especial', 'price': 199.90, 'category': esportes},
        {'name': 'Bola de Futebol', 'description': 'Bola oficial com certificação', 'price': 74.90, 'category': esportes},
        {'name': 'Bicicleta Mountain Bike', 'description': 'Bicicleta para trilhas', 'price': 1299.90, 'category': esportes},
        {'name': 'Esteira Elétrica', 'description': 'Esteira com 12 níveis de inclinação', 'price': 1899.90, 'category': esportes},
        {'name': 'Kit de Yoga', 'description': 'Tapete e acessórios para yoga', 'price': 129.90, 'category': esportes},
        {'name': 'Raquete de Tênis', 'description': 'Raquete profissional grafite', 'price': 249.90, 'category': esportes},
        {'name': 'Corda de Pular', 'description': 'Corda ajustável para cardio', 'price': 39.90, 'category': esportes},
        
        # Infantil
        {'name': 'Camiseta Infantil', 'description': 'Camiseta 100% algodão', 'price': 33.90, 'category': infantil},
        {'name': 'Meias Coloridas', 'description': 'Pacote com 5 pares de meias', 'price': 19.90, 'category': infantil},
        {'name': 'Sapatilha Infantil', 'description': 'Sapatilha para festas', 'price': 47.90, 'category': infantil},
        {'name': 'Carrinho de Controle Remoto', 'description': 'Carrinho com controle remoto', 'price': 89.90, 'category': infantil},
        {'name': 'Boneca Fashion', 'description': 'Boneca com acessórios e roupas', 'price': 129.90, 'category': infantil},
        {'name': 'Jogo Educativo', 'description': 'Jogo para desenvolver habilidades cognitivas', 'price': 69.90, 'category': infantil},
        {'name': 'Patins Infantil', 'description': 'Patins com rodas emborrachadas', 'price': 159.90, 'category': infantil},
        {'name': 'Mochila Escolar', 'description': 'Mochila com compartimentos e protetores', 'price': 79.90, 'category': infantil},
        
        # Beleza
        {'name': 'Kit Skincare', 'description': 'Rotina completa de cuidados faciais', 'price': 129.90, 'category': beleza},
        {'name': 'Secador de Cabelo', 'description': 'Secador profissional com 2200W', 'price': 199.90, 'category': beleza},
        {'name': 'Perfume Floral', 'description': 'Perfume feminino com notas florais', 'price': 249.00, 'category': beleza},
        {'name': 'Maquiagem Profissional', 'description': 'Kit completo de maquiagem', 'price': 159.90, 'category': beleza},
        {'name': 'Creme Hidratante', 'description': 'Hidratante corporal 500ml', 'price': 49.90, 'category': beleza},
        {'name': 'Barbeador Elétrico', 'description': 'Barbeador recarregável com 3 cabeças', 'price': 129.90, 'category': beleza},
        {'name': 'Esmalte Colorido', 'description': 'Esmalte de longa duração', 'price': 12.90, 'category': beleza},
        {'name': 'Protetor Solar', 'description': 'FPS 50 com filtro solar completo', 'price': 69.90, 'category': beleza},
        
        # Livros
        {'name': 'Romance Best-seller', 'description': 'Edição capa dura', 'price': 59.90, 'category': livros},
        {'name': 'Guia de Programação', 'description': 'Conceitos modernos de programação', 'price': 89.90, 'category': livros},
        {'name': 'Livro Infantil Ilustrado', 'description': 'Aprendizado divertido para crianças', 'price': 39.90, 'category': livros},
        {'name': 'Revista de Tecnologia', 'description': 'Edição mensal com as últimas tendências', 'price': 19.90, 'category': livros},
        {'name': 'Biografia Inspiradora', 'description': 'História de vida de grandes personalidades', 'price': 49.90, 'category': livros},
        {'name': 'Coleção Clássicos', 'description': '5 livros clássicos da literatura', 'price': 99.90, 'category': livros},
        {'name': 'Manual de Autoajuda', 'description': 'Técnicas para melhorar sua vida', 'price': 34.90, 'category': livros},
        {'name': 'HQ de Super-Herói', 'description': 'Edição especial com capa dura', 'price': 29.90, 'category': livros},
        
        # Automotivo
        {'name': 'Suporte para Celular', 'description': 'Universal para carro com carregamento rápido', 'price': 49.90, 'category': automotivo},
        {'name': 'Capa para Volante', 'description': 'Capa em couro ecológico', 'price': 69.90, 'category': automotivo},
        {'name': 'Calibrador Digital', 'description': 'Calibrador de pneus preciso', 'price': 119.90, 'category': automotivo},
        {'name': 'Aspirador de Pó Portátil', 'description': 'Aspirador para limpeza interna do carro', 'price': 89.90, 'category': automotivo},
        {'name': 'Organizador de Porta Copos', 'description': 'Porta copos com compartimentos', 'price': 29.90, 'category': automotivo},
        {'name': 'Capa Protetora para Carro', 'description': 'Capa resistente a chuva e sol', 'price': 199.90, 'category': automotivo},
        {'name': 'Adaptador Bluetooth', 'description': 'Adaptador para conectar dispositivos', 'price': 39.90, 'category': automotivo},
        {'name': 'Limpador de Vidros', 'description': 'Produto especial para limpeza de vidros automotivos', 'price': 19.90, 'category': automotivo},
        
        # Pet Shop
        {'name': 'Ração Premium', 'description': 'Ração para cães adultos sabor frango', 'price': 149.90, 'category': petshop},
        {'name': 'Cama para Pet', 'description': 'Cama ortopédica para cães médios', 'price': 129.90, 'category': petshop},
        {'name': 'Brinquedo Interativo', 'description': 'Brinquedo estimulante para gatos', 'price': 59.90, 'category': petshop},
        {'name': 'Coleira Ajustável', 'description': 'Coleira em nylon com placa de identificação', 'price': 39.90, 'category': petshop},
        {'name': 'Comedouro Duplo', 'description': 'Comedouro para água e ração', 'price': 49.90, 'category': petshop},
        {'name': 'Shampoo Neutro', 'description': 'Shampoo para todos os tipos de pelagem', 'price': 29.90, 'category': petshop},
        {'name': 'Arranhador para Gato', 'description': 'Arranhador em sisal com brinquedos', 'price': 89.90, 'category': petshop},
        {'name': 'Transporte para Pet', 'description': 'Caixa de transporte para viagens', 'price': 199.90, 'category': petshop},
        
        # Alimentos
        {'name': 'Cesta Gourmet', 'description': 'Produtos selecionados para degustação', 'price': 159.90, 'category': alimentos},
        {'name': 'Café Especial', 'description': 'Café torrado e moído premium', 'price': 29.90, 'category': alimentos},
        {'name': 'Chá Orgânico', 'description': 'Chá verde orgânico com propriedades antioxidantes', 'price': 24.90, 'category': alimentos},
        {'name': 'Chocolate Artesanal', 'description': 'Chocolate 70% cacau com frutas secas', 'price': 19.90, 'category': alimentos},
        {'name': 'Azeite Extravirgem', 'description': 'Azeite de oliva prensado a frio', 'price': 39.90, 'category': alimentos},
        {'name': 'Mel Natural', 'description': 'Mel de abelha 100% natural', 'price': 29.90, 'category': alimentos},
        {'name': 'Tempero Gourmet', 'description': 'Blend de ervas e especiarias', 'price': 14.90, 'category': alimentos},
        {'name': 'Castanha do Pará', 'description': 'Castanha fresca e crocante', 'price': 19.90, 'category': alimentos},
        
        # Ferramentas
        {'name': 'Furadeira Elétrica', 'description': 'Furadeira com velocidade ajustável', 'price': 219.90, 'category': ferramentas},
        {'name': 'Jogo de Chaves', 'description': 'Kit 24 peças com diferentes medidas', 'price': 79.90, 'category': ferramentas},
        {'name': 'Serra Circular', 'description': 'Serra com alta precisão e segurança', 'price': 349.90, 'category': ferramentas},
        {'name': 'Multímetro Digital', 'description': 'Medidor de voltagem, corrente e resistência', 'price': 89.90, 'category': ferramentas},
        {'name': 'Chave de Fenda', 'description': 'Conjunto profissional com 12 peças', 'price': 49.90, 'category': ferramentas},
        {'name': 'Martelo Profissional', 'description': 'Martelo com cabo emborrachado antiderrapante', 'price': 39.90, 'category': ferramentas},
        {'name': 'Nível Laser', 'description': 'Nível automático com precisão milimétrica', 'price': 129.90, 'category': ferramentas},
        {'name': 'Alicate Universal', 'description': 'Alicate multifuncional com corte lateral', 'price': 29.90, 'category': ferramentas},
        
        # Música
        {'name': 'Violão Acústico', 'description': 'Violão com tampo em spruce e encordoamento aço', 'price': 599.90, 'category': musica},
        {'name': 'Fone Monitor', 'description': 'Fone com som fiel para gravação', 'price': 299.90, 'category': musica},
        {'name': 'Teclado 61 Teclas', 'description': 'Teclado com funções educativas e sons realistas', 'price': 799.90, 'category': musica},
        {'name': 'Microfone Condensador', 'description': 'Microfone para estúdio com resposta de frequência ampla', 'price': 199.90, 'category': musica},
        {'name': 'Bateria Eletrônica', 'description': 'Bateria completa com módulo de som', 'price': 1299.90, 'category': musica},
        {'name': 'Pedal de Efeito', 'description': 'Pedal para guitarra com múltiplos efeitos', 'price': 149.90, 'category': musica},
        {'name': 'Cavaco', 'description': 'Cavaco afinado com cordas de nylon', 'price': 89.90, 'category': musica},
        {'name': 'Amplificador Guitarra', 'description': 'Amplificador de 20W com entrada para MP3', 'price': 399.90, 'category': musica},
        
        # Saúde
        {'name': 'Garrafa Térmica', 'description': 'Garrafa inox 1L mantém temperatura por 24h', 'price': 89.90, 'category': saude},
        {'name': 'Massageador Portátil', 'description': 'Massageador elétrico para alívio de tensões', 'price': 229.90, 'category': saude},
        {'name': 'Kit Elástico', 'description': 'Kit com 5 elásticos para exercícios em casa', 'price': 69.90, 'category': saude},
        {'name': 'Termômetro Digital', 'description': 'Termômetro infravermelho com medição rápida', 'price': 49.90, 'category': saude},
        {'name': 'Balança Digital', 'description': 'Balança com precisão de 100g e capacidade 150kg', 'price': 79.90, 'category': saude},
        {'name': 'Pulseira Fitness', 'description': 'Pulseira com monitoramento de batimentos cardíacos', 'price': 129.90, 'category': saude},
        {'name': 'Colchonete Yoga', 'description': 'Colchonete antiderrapante 6mm espessura', 'price': 59.90, 'category': saude},
        {'name': 'Cinta Modeladora', 'description': 'Cinta abdominal com compressão graduada', 'price': 39.90, 'category': saude},
        
        # Brinquedos
        {'name': 'Blocos de Montar', 'description': 'Kit criativo com 500 peças coloridas', 'price': 99.90, 'category': brinquedos},
        {'name': 'Quebra-cabeça 1000 peças', 'description': 'Quebra-cabeça com paisagem deslumbrante', 'price': 69.90, 'category': brinquedos},
        {'name': 'Lego Classic', 'description': 'Conjunto básico com peças variadas coloridas', 'price': 149.90, 'category': brinquedos},
        {'name': 'Boneca Interativa', 'description': 'Boneca que fala e se move com sensor de toque', 'price': 199.90, 'category': brinquedos},
        {'name': 'Carrinho de Controle Remoto', 'description': 'Carrinho com controle e bateria recarregável', 'price': 129.90, 'category': brinquedos},
        {'name': 'Jogo de Tabuleiro Familiar', 'description': 'Jogo estratégico para toda a família', 'price': 79.90, 'category': brinquedos},
        {'name': 'Pelúcia Gigante', 'description': 'Urso de pelúcia 1 metro de altura', 'price': 89.90, 'category': brinquedos},
        {'name': 'Kit de Pintura', 'description': 'Kit com tintas, pincéis e papel para artistas mirins', 'price': 49.90, 'category': brinquedos},
        
        # Papelaria
        {'name': 'Caderno Premium', 'description': 'Caderno pautado com 120 folhas capa dura', 'price': 19.90, 'category': papelaria},
        {'name': 'Canetas Coloridas', 'description': 'Kit com 10 cores variadas', 'price': 29.90, 'category': papelaria},
        {'name': 'Planner 2025', 'description': 'Agenda para organizar seu ano com stickers', 'price': 49.90, 'category': papelaria},
        {'name': 'Marca-texto Fluorescente', 'description': 'Conjunto com 5 cores fluorescentes', 'price': 19.90, 'category': papelaria},
        {'name': 'Clips Coloridos', 'description': 'Pacote com 100 unidades sortidas', 'price': 9.90, 'category': papelaria},
        {'name': 'Corretivo Líquido', 'description': 'Corretivo com ponta aplicadora precisa', 'price': 7.90, 'category': papelaria},
        {'name': 'Estojo Escolar', 'description': 'Estojo com zíper resistente e divisórias', 'price': 24.90, 'category': papelaria},
        {'name': 'Post-it Colorido', 'description': 'Notas adesivas com 4 formas diferentes', 'price': 14.90, 'category': papelaria},
    ]
    
    for prod_data in products_data:
        product, created = Product.objects.get_or_create(
            name=prod_data['name'],
            defaults=prod_data
        )
        if created:
            print(f"Created product: {product.name}")
        else:
            print(f"Product already exists: {product.name}")

if __name__ == '__main__':
    print("Populating categories...")
    populate_categories()
    
    print("\nPopulating products...")
    populate_products()
    
    print("\nData population completed!")