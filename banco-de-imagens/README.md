# Banco de Imagens do Rap Brasileiro

Este diretório contém uma coleção organizada de imagens relacionadas ao rap brasileiro, incluindo fotos de artistas, capas de álbuns, eventos históricos e elementos da cultura hip-hop no Brasil.

## Como usar este banco de imagens

1. Todas as imagens estão organizadas por categorias em subdiretórios
2. Os links diretos para as imagens estão listados nos arquivos markdown de cada categoria
3. Para baixar as imagens, você pode:
   - Clicar no link e salvar a imagem manualmente
   - Usar ferramentas como wget ou curl para baixar automaticamente
   - Utilizar scripts de download em lote (exemplos no final deste documento)

## Categorias de imagens

- [Artistas](artistas.md) - Fotos de rappers e grupos brasileiros
- [Álbuns](albuns.md) - Capas de álbuns históricos e importantes do rap nacional
- [Eventos](eventos.md) - Fotos de shows, batalhas de MCs e eventos históricos
- [Graffiti](graffiti.md) - Arte urbana relacionada à cultura hip-hop
- [Cultura](cultura.md) - Imagens representando a cultura hip-hop e rap no Brasil

## Direitos autorais e uso

Todas as imagens listadas neste repositório estão vinculadas às suas fontes originais. Ao usar estas imagens, lembre-se de:

1. Verificar os direitos autorais de cada imagem
2. Dar os devidos créditos aos fotógrafos e artistas
3. Respeitar os termos de uso da fonte original da imagem
4. Usar apenas para fins educacionais, jornalísticos ou de pesquisa conforme permitido

## Como baixar imagens em lote

### Usando wget (Linux/Mac/Windows com WSL)

Para baixar todas as imagens de uma categoria específica:

```bash
# Crie um diretório para salvar as imagens
mkdir -p imagens/artistas

# Execute o wget para baixar as imagens (substitua o URL)
wget -i urls_artistas.txt -P imagens/artistas
```

### Usando Python

Você também pode usar este script Python para baixar imagens:

```python
import os
import requests
from urllib.parse import urlparse

# Lista de URLs das imagens
urls = [
    'https://exemplo.com/imagem1.jpg',
    'https://exemplo.com/imagem2.jpg',
    # Adicione mais URLs aqui
]

# Diretório para salvar as imagens
output_dir = 'imagens_baixadas'
os.makedirs(output_dir, exist_ok=True)

# Baixar cada imagem
for url in urls:
    try:
        # Extrair o nome do arquivo da URL
        filename = os.path.basename(urlparse(url).path)
        
        # Caminho completo para salvar
        filepath = os.path.join(output_dir, filename)
        
        # Baixar a imagem
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Verificar erros
        
        # Salvar a imagem
        with open(filepath, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
                
        print(f"Imagem baixada: {filename}")
        
    except Exception as e:
        print(f"Erro ao baixar {url}: {e}")
```

## Contribuição

Sinta-se à vontade para contribuir com este banco de imagens adicionando:

1. Novos links para imagens relevantes
2. Categorias adicionais
3. Informações e contexto sobre as imagens
4. Correções ou melhorias na organização

Lembre-se de sempre respeitar os direitos autorais e incluir as fontes das imagens.