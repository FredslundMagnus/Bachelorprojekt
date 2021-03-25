
# Parameters

    Name :                      causal3_9x9-3
    Main :                      teleport
    Level :                     Levels.Causal3
    Hours :                     12.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    Network2 :                  Networks.Mini
    Learner1 :                  Learners.Qlearn
    Learner2 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Exploration2 :              Explorations.epsilonGreedy
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                False
    Layer door :                False
    Layer holder :              False
    Layer putter :              False
    Layer rock :                False
    Layer dirt :                True
    Layer diamond1 :            False
    Layer diamond2 :            False
    Layer diamond3 :            False
    Layer diamond4 :            False
    Layer reddoors :            True
    Layer redkeys :             True
    Layer bluedoors :           True
    Layer bluekeys :            True
    K :                         200000
    Epsilon cap :               0.1
    Softmax cap :               0.025
    Gamma :                     0.98
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.04
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      40346030975 function calls (40174298672 primitive calls) in 42916.49 seconds

##    Ordered by: cumulative time
   List reduced from 475 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42916.489 42916.489 {built-in method builtins.exec}
                      1    1.923    1.923 42916.489 42916.489 <string>:1(<module>)
                      1  138.985  138.985 42914.565 42914.565 main.py:43(teleport)
                6133770   20.463    0.000 13192.059    0.002 agent.py:27(learn)
                3066885   11.248    0.000 12742.030    0.004 game.py:27(step)
                3066885   16.953    0.000 12087.350    0.004 layers.py:475(step)
                6133770  348.713    0.000 11085.919    0.002 learner.py:42(Qlearn)
                3066885  102.350    0.000 7925.411    0.003 agent.py:51(_learn)
                3066885  231.703    0.000 7881.631    0.003 layers.py:18(step)
              306688500  358.474    0.000 7623.552    0.000 layer.py:76(move)
        193198298/21467006  711.480    0.000 5889.587    0.000 module.py:866(_call_impl)
               15333236   42.397    0.000 5465.405    0.000 network.py:24(forward)
                3066885 3156.842    0.001 5397.956    0.002 replaybuffer.py:27(teleporter_save_data)
               15333236  174.683    0.000 5329.321    0.000 container.py:117(forward)
                3066885   85.075    0.000 5233.564    0.002 agent.py:110(_learn)
              306688500  780.684    0.000 4608.559    0.000 layers.py:492(check)
                6133770   49.772    0.000 4232.696    0.001 optimizer.py:84(wrapper)
                3066886  312.141    0.000 4167.266    0.001 layers.py:446(update)
                3066885 2240.409    0.001 4044.037    0.001 agent.py:81(interveen)
                6133770   25.403    0.000 4012.415    0.001 grad_mode.py:24(decorate_context)
                6133770  161.361    0.000 3931.692    0.001 adam.py:55(step)
                6132581  141.658    0.000 3674.117    0.001 agent.py:46(__call__)
                6133770  821.379    0.000 3578.561    0.001 _functional.py:53(adam)
                3066885 2581.746    0.001 3562.292    0.001 replaybuffer.py:23(sample_data)
                6133770   23.057    0.000 2926.173    0.000 tensor.py:195(backward)
                6133770   22.913    0.000 2902.245    0.000 __init__.py:68(backward)
                6133770 2765.357    0.000 2765.357    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
              306688500  464.427    0.000 2327.868    0.000 layers.py:486(isFree)
               30666472   65.311    0.000 2010.355    0.000 conv.py:398(forward)
               30666472   38.649    0.000 1916.579    0.000 conv.py:390(_conv_forward)
               30666472 1877.929    0.000 1877.929    0.000 {built-in method conv2d}
                3066885 1119.628    0.000 1876.122    0.001 agent.py:63(modify)
              223163328 1870.171    0.000 1870.171    0.000 {built-in method clone}
             2377669223 1505.708    0.000 1863.441    0.000 layer.py:73(isFree)
               27601974  965.454    0.000 1706.702    0.000 layer.py:137(NoRock_update)
               39865938   77.498    0.000 1495.151    0.000 linear.py:93(forward)
               39865938   31.682    0.000 1379.551    0.000 functional.py:1737(linear)
               39865938 1340.620    0.000 1340.620    0.000 {built-in method torch._C._nn.linear}
                4729537   48.343    0.000 1275.261    0.000 layers.py:496(restart)
                3066885   41.477    0.000 1141.351    0.000 agent.py:105(__call__)
                9199466   51.965    0.000 1131.158    0.000 agent.py:55(modify_board)
             4550769427  755.793    0.000 1075.085    0.000 enum.py:646(__hash__)
               12667349  939.942    0.000  939.942    0.000 {built-in method tensor}
               27600776  937.256    0.000  937.256    0.000 {built-in method cat}
              306688500  587.695    0.000  930.149    0.000 layers.py:302(check)
              306688500  539.242    0.000  885.681    0.000 layers.py:261(check)
                4729537   22.410    0.000  819.795    0.000 level.py:8(__init__)
               55199174   41.472    0.000  788.117    0.000 activation.py:713(forward)
                6133770    6.510    0.000  779.650    0.000 game.py:23(board)
                3066885   54.769    0.000  767.585    0.000 replaybuffer.py:19(stacker)
              306688600   83.177    0.000  759.438    0.000 {built-in method builtins.all}
                9199466  749.264    0.000  749.264    0.000 {built-in method torch._C._nn.one_hot}
               55199174   45.628    0.000  746.645    0.000 functional.py:1364(leaky_relu)
              941111512  212.104    0.000  710.396    0.000 layers.py:452(<genexpr>)
                4729537  120.059    0.000  709.890    0.000 levels.py:163(generate)
               55199174  691.678    0.000  691.678    0.000 {built-in method torch._C._nn.leaky_relu}
              110407860  682.975    0.000  682.975    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                6133770  113.405    0.000  636.460    0.000 optimizer.py:189(zero_grad)
              110407860  618.613    0.000  618.613    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              306688500  428.973    0.000  579.964    0.000 layers.py:63(check)
              306688500  324.647    0.000  503.170    0.000 layers.py:328(check)
             5947121634  501.126    0.000  501.126    0.000 layer.py:69(positions)
             1203699233  480.478    0.000  480.478    0.000 layer.py:116(elements)
                9459074   59.072    0.000  475.520    0.000 level.py:41(notUsed)
              306688600  313.532    0.000  470.727    0.000 layers.py:110(isDone)
              306688500  296.604    0.000  463.358    0.000 layers.py:287(check)
              232362794  435.606    0.000  435.606    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                3066885  251.114    0.000  429.589    0.000 collector.py:54(collect)
               55203930  414.595    0.000  414.595    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               42565833   53.904    0.000  393.784    0.000 layer.py:50(restart)
              306688500  259.960    0.000  391.958    0.000 layers.py:47(check)
                6132581  138.049    0.000  370.560    0.000 exploration.py:53(softmaxer)
               55203930  361.981    0.000  361.981    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               55203930  333.252    0.000  333.252    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               55203930  332.496    0.000  332.496    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
             4550791858  319.295    0.000  319.295    0.000 {built-in method builtins.hash}
              575425984  220.172    0.000  299.501    0.000 layer.py:100(add)
              386427564  240.580    0.000  299.292    0.000 tensor.py:906(grad)
               12525959  101.775    0.000  268.425    0.000 random.py:315(sample)
                6133770    7.818    0.000  249.393    0.000 loss.py:527(forward)
               55203930  248.544    0.000  248.544    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                6133770   23.610    0.000  241.574    0.000 functional.py:2898(mse_loss)
        2922927740/2922927738  200.360    0.000  239.948    0.000 {built-in method builtins.len}
              198643719  239.471    0.000  239.471    0.000 level.py:32(inverse)
                4729637  112.505    0.000  225.636    0.000 layers.py:33(reset)
              303937043  142.183    0.000  220.915    0.000 layer.py:96(remove)
             1853979185  204.532    0.000  204.532    0.000 layer.py:177(isBlocking)
               18401310  186.123    0.000  186.123    0.000 {built-in method sum}
                6133770  147.538    0.000  147.538    0.000 {built-in method torch._C._nn.mse_loss}
              220479071   98.111    0.000  141.711    0.000 random.py:250(_randbelow_with_getrandbits)
             1884802517  139.732    0.000  139.732    0.000 {method 'append' of 'list' objects}
               30666472   22.235    0.000  139.498    0.000 flatten.py:39(forward)
                9459074    8.772    0.000  137.789    0.000 level.py:38(elementsIn)
                6134689  134.837    0.000  134.837    0.000 {built-in method max}
                9200655   11.641    0.000  127.217    0.000 tensor.py:525(__rsub__)
               30666472  117.263    0.000  117.263    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                6132581  117.184    0.000  117.184    0.000 {built-in method multinomial}
                9200655  113.444    0.000  113.444    0.000 {built-in method rsub}
                6133770   22.766    0.000  109.128    0.000 __init__.py:28(_make_grads)
                3066885   11.655    0.000  108.534    0.000 exploration.py:47(epsilonGreedy)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 9458197: <causal3_9x9_3> in cluster <dcc> Done

Job <causal3_9x9_3> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Mar 25 01:18:04 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Mar 25 01:18:05 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Mar 25 01:18:05 2021
Terminated at Thu Mar 25 13:13:32 2021
Results reported at Thu Mar 25 13:13:32 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=8G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   42803.82 sec.
    Max Memory :                                 6849 MB
    Average Memory :                             4905.67 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               1343.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42950 sec.
    Turnaround time :                            42928 sec.

The output (if any) is above this job summary.

