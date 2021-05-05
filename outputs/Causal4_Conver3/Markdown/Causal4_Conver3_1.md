
# Parameters

    Name :                      Causal4_Conver3-1
    Main :                      CFagent
    Level :                     Levels.Causal4
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      76765612131 function calls (76425595936 primitive calls) in 86109.57 seconds

##    Ordered by: cumulative time
   List reduced from 513 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86109.573 86109.573 {built-in method builtins.exec}
                      1    4.404    4.404 86109.573 86109.573 <string>:1(<module>)
                      1  380.522  380.522 86105.169 86105.169 main.py:80(CFagent)
               10736964   37.132    0.000 24582.567    0.002 agent.py:29(learn)
                3578988   15.716    0.000 21747.304    0.006 game.py:42(step)
                3578988   20.866    0.000 20946.986    0.006 layers.py:827(step)
               10736955  628.080    0.000 19937.985    0.002 learner.py:42(Qlearn)
                3578988  297.574    0.000 13824.881    0.004 layers.py:17(step)
              357849151  939.827    0.000 13497.039    0.000 layer.py:106(move)
        380278997/40264493 1433.912    0.000 11739.591    0.000 module.py:866(_call_impl)
               29527538   76.985    0.000 10994.758    0.000 network.py:28(forward)
                3578988 1021.283    0.000 10981.881    0.003 agent.py:212(counterfact)
               29527538  356.721    0.000 10735.831    0.000 container.py:117(forward)
                3578988  367.231    0.000 9560.936    0.003 agent.py:54(_learn)
                3578988  362.687    0.000 8771.687    0.002 agent.py:204(_learn)
              357849151 1656.204    0.000 8326.182    0.000 layers.py:844(check)
               10736955   83.985    0.000 7715.163    0.001 optimizer.py:84(wrapper)
               10736955   44.717    0.000 7341.769    0.001 grad_mode.py:24(decorate_context)
               10736955  304.325    0.000 7202.382    0.001 adam.py:55(step)
                3578989  510.141    0.000 7072.937    0.002 layers.py:793(update)
               10736955 1503.010    0.000 6544.699    0.001 _functional.py:53(adam)
                3578988  104.186    0.000 6190.416    0.002 agent.py:117(_learn)
                3578988 5117.960    0.001 6181.397    0.002 replaybuffer.py:22(sample_data)
                3578988 4955.302    0.001 5976.939    0.002 replaybuffer.py:67(sample_data)
               57928851 5815.159    0.000 5815.159    0.000 {built-in method tensor}
                9393655  233.479    0.000 5718.178    0.001 agent.py:49(__call__)
               49714425   29.151    0.000 5628.594    0.000 game.py:38(board)
                3578988 2957.975    0.001 5170.519    0.001 replaybuffer.py:28(teleporter_save_data)
               10736955   40.505    0.000 5159.761    0.000 tensor.py:195(backward)
               10736955   39.891    0.000 5118.022    0.000 __init__.py:68(backward)
               10736955 4880.989    0.000 4880.989    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3578988 2543.085    0.001 4713.843    0.001 agent.py:88(interveen)
               71579770 2639.496    0.000 4473.720    0.000 layer.py:159(update)
               59055076  125.630    0.000 3989.681    0.000 conv.py:398(forward)
               59055076   81.086    0.000 3803.620    0.000 conv.py:390(_conv_forward)
               59055076 3722.534    0.000 3722.534    0.000 {built-in method conv2d}
              357849151  664.045    0.000 3541.607    0.000 layers.py:838(isFree)
               81424638  158.766    0.000 3034.668    0.000 linear.py:93(forward)
             3429279839 2367.457    0.000 2877.562    0.000 layer.py:103(isFree)
                2238961   43.837    0.000 2798.182    0.001 agent.py:176(choose_action)
               81424638   65.611    0.000 2793.170    0.000 functional.py:1737(linear)
               81424638 2713.063    0.000 2713.063    0.000 {built-in method torch._C._nn.linear}
                3578988 1645.975    0.000 2489.586    0.001 agent.py:67(modify)
              230972226 2094.029    0.000 2094.029    0.000 {built-in method clone}
             7276207310 1261.711    0.000 1819.012    0.000 enum.py:646(__hash__)
               48762478 1737.867    0.000 1737.867    0.000 {built-in method cat}
                4527611   53.923    0.000 1644.112    0.000 layers.py:849(restart)
              110952176   84.666    0.000 1604.155    0.000 activation.py:713(forward)
               12972643   79.607    0.000 1593.795    0.000 agent.py:59(modify_board)
              356950278  349.222    0.000 1568.250    0.000 {built-in method builtins.any}
              110952176   89.908    0.000 1519.489    0.000 functional.py:1364(leaky_relu)
                3578979   58.284    0.000 1518.600    0.000 agent.py:172(__call__)
                3578988   54.490    0.000 1439.040    0.000 agent.py:112(__call__)
              110952176 1412.961    0.000 1412.961    0.000 {built-in method torch._C._nn.leaky_relu}
                3578988 1048.385    0.000 1349.094    0.000 replaybuffer.py:73(CF_save_data)
              357849151  975.706    0.000 1299.841    0.000 layers.py:77(check)
              200423148 1286.027    0.000 1286.027    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             3887084179 1003.756    0.000 1219.028    0.000 layers.py:809(<genexpr>)
              357849151  762.644    0.000 1217.604    0.000 layers.py:286(check)
                4527611   23.863    0.000 1178.209    0.000 level.py:8(__init__)
               10736955  208.127    0.000 1159.759    0.000 optimizer.py:189(zero_grad)
              200423148 1128.230    0.000 1128.230    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              357849151  659.105    0.000 1107.865    0.000 layers.py:246(check)
               12972643 1053.322    0.000 1053.322    0.000 {built-in method torch._C._nn.one_hot}
             1379686634 1039.549    0.000 1039.549    0.000 layer.py:154(elements)
                4527611  140.931    0.000  939.704    0.000 levels.py:199(generate)
             9351475535  824.514    0.000  824.514    0.000 layer.py:99(positions)
                3578988   65.936    0.000  813.509    0.000 replaybuffer.py:18(stacker)
              357898900   67.357    0.000  800.357    0.000 {built-in method builtins.all}
                3578979   65.554    0.000  780.805    0.000 replaybuffer.py:63(stacker)
              741865172  157.530    0.000  775.438    0.000 layers.py:799(<genexpr>)
              100211574  749.653    0.000  749.653    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              357849151  527.358    0.000  703.027    0.000 layers.py:62(check)
              100211574  665.388    0.000  665.388    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                9055222   75.223    0.000  661.745    0.000 level.py:41(notUsed)
        9401191818/9401191815  578.777    0.000  642.661    0.000 {built-in method builtins.len}
              357849151  412.194    0.000  628.798    0.000 layers.py:273(check)
              357898900  414.652    0.000  614.366    0.000 layers.py:113(isDone)
              100211574  605.252    0.000  605.252    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              100211574  581.501    0.000  581.501    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                9393655  211.161    0.000  565.446    0.000 exploration.py:53(softmaxer)
              357849151  349.624    0.000  560.989    0.000 layers.py:313(check)
             7276247997  557.309    0.000  557.309    0.000 {built-in method builtins.hash}
              701481102  444.503    0.000  549.572    0.000 tensor.py:906(grad)
               16213198  207.115    0.000  544.502    0.000 random.py:315(sample)
                3578988  301.522    0.000  514.950    0.000 collector.py:46(collect)
              247523848  480.852    0.000  480.852    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                2238961  447.748    0.000  473.369    0.000 agent.py:187(convert_values)
              100211574  459.466    0.000  459.466    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              357849151  300.653    0.000  450.817    0.000 layers.py:48(check)
               10736955   14.348    0.000  429.857    0.000 loss.py:527(forward)
               10736955   39.658    0.000  415.509    0.000 functional.py:2898(mse_loss)
               45276110   59.859    0.000  397.942    0.000 layer.py:77(restart)
              357849151  250.619    0.000  371.341    0.000 layers.py:23(check)
              366560365  270.802    0.000  370.988    0.000 layer.py:134(remove)
              620071712  246.649    0.000  336.820    0.000 layer.py:138(add)
             3953552131  299.548    0.000  299.548    0.000 {method 'random' of '_random.Random' objects}
              461964646  197.998    0.000  288.539    0.000 random.py:250(_randbelow_with_getrandbits)
                9055222   10.068    0.000  275.669    0.000 level.py:38(elementsIn)
             2765030976  274.468    0.000  274.468    0.000 layer.py:211(isBlocking)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9606151: <Causal4_Conver3_1> in cluster <dcc> Done

Job <Causal4_Conver3_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 01:44:21 2021
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon May  3 20:29:06 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 20:29:06 2021
Terminated at Tue May  4 20:24:20 2021
Results reported at Tue May  4 20:24:20 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85906.77 sec.
    Max Memory :                                 9944 MB
    Average Memory :                             6572.99 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6440.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86115 sec.
    Turnaround time :                            153599 sec.

The output (if any) is above this job summary.

