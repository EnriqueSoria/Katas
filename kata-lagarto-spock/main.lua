--[[---------------------------------------------- 
            Vocabulary and logic 
----------------------------------------------]]-- 
voc = { 'piedra', 'papel', 'tijeras', 'lagarto', 'spock' } 

who =  
  {
      tijeras = { papel   = 'Tijeras cortan papel', 
                  lagarto = 'Tijeras decapitan al lagarto'}, 
      papel   = { piedra  = 'Papel cubre a piedra', 
                  spock   = 'Papel desautoriza a Spock'}, 
      piedra  = { lagarto = 'Piedra aplasta a lagarto', 
                  tijeras = 'Piedra aplasta las tijeras'}, 
      lagarto = { spock   = 'Lagarto envenena a Spock', 
                  papel   = 'Lagarto se come el papel'}, 
      spock   = { tijeras = 'Spock destroza las tijeras', 
                  piedra  = 'Spock vaporiza la piedra'} 
  }

--[[---------------------------------------------- 
            Main activity 
----------------------------------------------]]-- 

math.randomseed(os.time())  

print ( 'Choose one: \n'  .. 
            '\tPiedra\n'  .. 
            '\tPapel\n'   .. 
            '\tTijeras\n' .. 
            '\tLagarto\n' .. 
            '\tSpock' 
      ) 

user  = string.lower( io.read( '*line' ) ) 
cpu   = math.random ( 0, 4 ) 
cpu   = voc [ cpu ] 

if user == cpu then 
    print 'Empate' 
else 
  if who [ cpu ][ user ] ~= nil then 
    print ( who [ cpu ] [ user ] )  
  else 
    print ( who [ user ] [ cpu ] )  
  end 
end 
