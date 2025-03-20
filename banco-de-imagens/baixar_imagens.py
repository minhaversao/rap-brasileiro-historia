#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script para baixar imagens para o banco de imagens do rap brasileiro.
Este script pode ser usado para baixar imagens de sites que permitem uso livre.
"""

import os
import sys
import requests
from urllib.parse import urlparse

def criar_diretorios():
    """Cria os diretórios necessários para armazenar as imagens."""
    diretorios = [
        'imagens/artistas',
        'imagens/albuns',
        'imagens/graffiti'
    ]
    
    for diretorio in diretorios:
        os.makedirs(diretorio, exist_ok=True)
        print(f"Diretório {diretorio} criado ou já existente.")
    
    return True

def baixar_imagem(url, destino):
    """Baixa uma imagem da URL especificada e salva no destino.
    
    Args:
        url (str): URL da imagem a ser baixada
        destino (str): Caminho completo onde a imagem será salva
    
    Returns:
        bool: True se o download for bem-sucedido, False caso contrário
    """
    try:
        # Extrair o nome do arquivo da URL
        nome_arquivo = os.path.basename(urlparse(url).path)
        
        # Se nenhum nome de arquivo for fornecido, use o nome original
        if not os.path.basename(destino):
            destino = os.path.join(destino, nome_arquivo)
        
        # Verifica se o diretório de destino existe
        diretorio_destino = os.path.dirname(destino)
        if not os.path.exists(diretorio_destino):
            os.makedirs(diretorio_destino, exist_ok=True)
        
        # Baixa a imagem
        print(f"Baixando {url} para {destino}...")
        resposta = requests.get(url, stream=True)
        resposta.raise_for_status()  # Lança erro se o download falhar
        
        # Salva a imagem
        with open(destino, 'wb') as arquivo:
            for chunk in resposta.iter_content(chunk_size=8192):
                arquivo.write(chunk)
        
        print(f"Imagem salva em {destino}")
        return True
    
    except Exception as e:
        print(f"Erro ao baixar {url}: {e}")
        return False

def baixar_lista_de_imagens(arquivo_lista):
    """Baixa uma lista de imagens de um arquivo.
    
    O arquivo deve conter uma URL por linha, opcionalmente seguida por um
    caminho de destino separado por um espaço.
    
    Args:
        arquivo_lista (str): Caminho para o arquivo com a lista de URLs
    
    Returns:
        int: Número de imagens baixadas com sucesso
    """
    if not os.path.exists(arquivo_lista):
        print(f"Arquivo {arquivo_lista} não encontrado.")
        return 0
    
    sucesso = 0
    with open(arquivo_lista, 'r') as f:
        for linha in f:
            linha = linha.strip()
            if not linha or linha.startswith('#'):
                continue
            
            partes = linha.split(' ', 1)
            url = partes[0]
            destino = partes[1] if len(partes) > 1 else None
            
            if destino is None:
                # Se o destino não for especificado, use o nome do arquivo da URL
                nome_arquivo = os.path.basename(urlparse(url).path)
                destino = os.path.join('imagens', 'artistas', nome_arquivo)
            
            if baixar_imagem(url, destino):
                sucesso += 1
    
    return sucesso

def main():
    """Função principal que executa o script."""
    print("Banco de Imagens do Rap Brasileiro - Ferramenta de Download")
    print("=" * 60)
    
    # Cria os diretórios necessários
    criar_diretorios()
    
    if len(sys.argv) > 1:
        # Se um argumento for fornecido, assume que é uma URL
        if sys.argv[1].startswith('http'):
            url = sys.argv[1]
            destino = sys.argv[2] if len(sys.argv) > 2 else None
            
            if destino is None:
                nome_arquivo = os.path.basename(urlparse(url).path)
                destino = os.path.join('imagens', 'artistas', nome_arquivo)
            
            baixar_imagem(url, destino)
        
        # Se o argumento for um arquivo, assume que é uma lista de URLs
        elif os.path.exists(sys.argv[1]):
            arquivo_lista = sys.argv[1]
            num_baixados = baixar_lista_de_imagens(arquivo_lista)
            print(f"{num_baixados} imagens foram baixadas com sucesso.")
        
        else:
            print(f"Argumento inválido: {sys.argv[1]}")
            print("Use uma URL ou o caminho para um arquivo com lista de URLs.")
    
    else:
        # Se nenhum argumento for fornecido, exibe instruções
        print("\nUso:")
        print("  python baixar_imagens.py [URL] [destino]")
        print("  python baixar_imagens.py [arquivo_lista]")
        print("\nExemplos:")
        print("  python baixar_imagens.py https://exemplo.com/imagem.jpg")
        print("  python baixar_imagens.py https://exemplo.com/imagem.jpg imagens/artistas/minha_imagem.jpg")
        print("  python baixar_imagens.py lista_urls.txt")
        print("\nFormato do arquivo de lista:")
        print("  # Comentário")
        print("  https://exemplo.com/imagem1.jpg")
        print("  https://exemplo.com/imagem2.jpg imagens/albuns/album.jpg")

if __name__ == "__main__":
    main()