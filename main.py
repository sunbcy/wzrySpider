"""
########################################################
#        Program to Download Wallpapers from           #
#     http://pvp.qq.com/web201605/wallpaper.shtml      #
#                                                      #
#    reference: https://www.jianshu.com/p/395354e3d9ef #
#                                                      #
#                 Author - CQ                          #
#                                                      #
#                 dated - 2018-1-8 14:28:52            #
#                 Update - 2018-1-16 14:54:30          #
########################################################

"""
from src.app.wzry_wall_dl import WzrzWallDL

def main():
    """mail"""
    wzrz_wall_dl = WzrzWallDL()
    wzrz_wall_dl.wzrz_wall_dl()

if __name__ == '__main__':
    main()
