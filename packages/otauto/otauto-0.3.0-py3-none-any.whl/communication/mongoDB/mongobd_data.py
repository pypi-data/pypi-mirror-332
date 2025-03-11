"""
MongoDB数据库信息
角色role_id为唯一标识
"""

#设备信息
collection_facility = {"vnc_port": None, # vnc端口
                       "vnc_ip": None, # vnc ip
                       "role_id": None, # 角色id
                       "role_name":None, # 角色名称
                       "updated_at":None, # 更新时间
                       }
#角色信息
collection_role = {"vnc_port": None, # vnc端口
                   "vnc_ip": None,  # vnc ip
                   "role_id": None, # 角色id
                   "role_name":None, # 角色名称
                   "role_level": None, # 等级
                   "role_sect": None, # 角色门派
                   "role_factions": None, # 角色阵营
                   "role_gang" : None, # 角色帮派
                   "role_scoring":None, # 角色评分
                   "role_position":None, # 角色位置
                   "bound_currency":None, # 绑定的货币
                   "unbound_currency":None, # 未绑定的货币
                   "updated_at":None, # 更新
                   }
#任务信息
collection_task = {"vnc_port": None, # vnc端口
                   "vnc_ip": None, # vnc ip
                   "role_id": None, # 角色id
                   "role_name":None, # 角色名称
                   "task_current": None,  # 当前任务
                   "task_finish": None, # 完成任务,是个列表
                   "date": None,  # 任务日期,用于每日初始化这个集合
                   "updated_at":None, # 更新
                   }

#异常信息
collection_exception = {"vnc_port": None, # vnc端口
                        "vnc_ip": None, # vnc ip
                        "role_id": None, # 角色id
                        "role_name":None, # 角色名称
                        "exception_num": None, # 异常代码
                        "exception_info":None, # 异常信息
                        "updated_at":None, # 更新
                        }

#装备信息
collection_gear = {"vnc_port": None, # vnc端口
                        "vnc_ip": None, # vnc ip
                        "role_id": None, # 角色id
                        "role_name":None, # 角色名称
                        "武器": None, #(进阶等级,强化等级)
                        "头盔": None, #(进阶等级,强化等级)
                        "衣服": None, #(进阶等级,强化等级)
                        "护手":None,   #(进阶等级,强化等级)
                        "腰带":None,   #(进阶等级,强化等级)
                        "鞋子": None, #(进阶等级,强化等级)
                        "项链": None, #(进阶等级,强化等级)
                        "玉佩": None, #(进阶等级,强化等级)
                        "戒指上": None, #(进阶等级,强化等级)
                        "戒指下":None, #(进阶等级,强化等级)
                        "护身符左": None, #(进阶等级,强化等级)
                        "护身符右":None,   #(进阶等级,强化等级)
                        "秘籍": None, #(进阶等级,强化等级)
                        "updated_at":None, # 更新
                        }

#宠物信息
collection_pet = {"vnc_port": None, # vnc端口
                 "vnc_ip": None, # vnc ip
                 "role_id": None, # 角色id
                 "role_name":None, # 角色名称
                  "pet_name" : None, # 宠物名称
                 "updated_at":None, # 更新
                 }

#替换为你的集合名称
collection_dict= {
                "collection_facility":collection_facility,
                "collection_role":collection_role,
                "collection_task":collection_task,
                "collection_equipment":collection_gear,
                "collection_exception":collection_exception,
                "collection_pet":collection_pet,
                }

