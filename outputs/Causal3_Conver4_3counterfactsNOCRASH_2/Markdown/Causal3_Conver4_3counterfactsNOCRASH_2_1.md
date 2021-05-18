
# Parameters

    Name :                      Causal3_Conver4_3counterfactsNOCRASH_2-1
    Main :                      Load_Cfagent
    Level :                     Levels.Causal3
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     11.0
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
    Cf convert :                4
    Counterfacts :              3
    Topn :                      5
    Random counterfacts :       False
    Num :                       1
    Load name :                 Causal3_Conver4_3counterfactsNOCRASH
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      56298317326 function calls (55937214097 primitive calls) in 86153.13 seconds

##    Ordered by: cumulative time
   List reduced from 433 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86153.128 86153.128 {built-in method builtins.exec}
                      1    3.889    3.889 86153.128 86153.128 <string>:1(<module>)
                      1  261.806  261.806 86149.239 86149.239 main.py:109(Load_Cfagent)
                2545216 3622.619    0.001 25977.085    0.010 agent.py:212(counterfact)
                7635648   27.979    0.000 23064.879    0.003 agent.py:29(learn)
                7635648  561.393    0.000 19334.967    0.003 learner.py:42(Qlearn)
        399676162/38575754 1648.275    0.000 14473.899    0.000 module.py:866(_call_impl)
               30940106   86.600    0.000 13762.925    0.000 network.py:28(forward)
               30940106  475.053    0.000 13479.137    0.000 container.py:117(forward)
                2545216   12.461    0.000 13030.079    0.005 game.py:42(step)
                2545216   15.605    0.000 12455.632    0.005 layers.py:827(step)
                6565426  136.809    0.000 10124.095    0.002 agent.py:176(choose_action)
               96033994 8915.078    0.000 8915.078    0.000 {built-in method tensor}
                2545216  241.419    0.000 8870.888    0.003 agent.py:54(_learn)
               90419949   56.939    0.000 8794.506    0.000 game.py:38(board)
               11648600  269.225    0.000 8261.375    0.001 agent.py:49(__call__)
                2545216  239.878    0.000 8244.328    0.003 agent.py:204(_learn)
                7635648   68.396    0.000 8092.451    0.001 optimizer.py:84(wrapper)
                7635648   32.422    0.000 7771.374    0.001 grad_mode.py:24(decorate_context)
                7635648  231.945    0.000 7666.108    0.001 adam.py:55(step)
                2545216  210.442    0.000 7240.001    0.003 layers.py:17(step)
                7635648 1554.730    0.000 7187.317    0.001 _functional.py:53(adam)
              254441789  401.021    0.000 7005.828    0.000 layer.py:106(move)
                2545216   70.224    0.000 5905.560    0.002 agent.py:117(_learn)
                2545216  354.342    0.000 5179.910    0.002 layers.py:793(update)
                7635648   35.859    0.000 5026.300    0.001 tensor.py:195(backward)
                7635648   31.466    0.000 4989.318    0.001 __init__.py:68(backward)
                7635648 4786.921    0.001 4786.921    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               61880212  146.439    0.000 4762.297    0.000 conv.py:398(forward)
                2545216 2484.275    0.001 4622.036    0.002 replaybuffer.py:28(teleporter_save_data)
               61880212   92.611    0.000 4549.278    0.000 conv.py:390(_conv_forward)
               61880212 4456.667    0.000 4456.667    0.000 {built-in method conv2d}
                2545216 3590.483    0.001 4374.176    0.002 replaybuffer.py:22(sample_data)
               81446896 2344.535    0.000 4350.341    0.000 layer.py:175(NoRock_update)
                2545216 3554.554    0.001 4331.065    0.002 replaybuffer.py:67(sample_data)
                2545216 2341.507    0.001 4142.219    0.002 agent.py:88(interveen)
              254441789  879.817    0.000 4118.166    0.000 layers.py:844(check)
               87729886  189.954    0.000 3921.923    0.000 linear.py:93(forward)
               87729886   71.767    0.000 3638.416    0.000 functional.py:1737(linear)
               87729886 3548.839    0.000 3548.839    0.000 {built-in method torch._C._nn.linear}
                2545216 1576.177    0.001 2313.341    0.001 agent.py:67(modify)
              118669992  101.823    0.000 2174.628    0.000 activation.py:713(forward)
              170090017 2170.463    0.000 2170.463    0.000 {built-in method clone}
                6565426 1824.664    0.000 2127.600    0.000 agent.py:187(convert_values)
              254441789  389.832    0.000 2108.447    0.000 layers.py:838(isFree)
              118669992   99.259    0.000 2072.805    0.000 functional.py:1364(leaky_relu)
               14193816   95.514    0.000 2022.615    0.000 agent.py:59(modify_board)
              118669992 1951.574    0.000 1951.574    0.000 {built-in method torch._C._nn.leaky_relu}
                2545216 1373.790    0.001 1886.200    0.001 replaybuffer.py:73(CF_save_data)
                5892942   59.778    0.000 1880.775    0.000 layers.py:849(restart)
             1960514460 1429.336    0.000 1718.615    0.000 layer.py:103(isFree)
               39645976 1542.822    0.000 1542.822    0.000 {built-in method cat}
              142532096 1472.837    0.000 1472.837    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                5892942   29.293    0.000 1364.060    0.000 level.py:8(__init__)
               14193816 1288.841    0.000 1288.841    0.000 {built-in method torch._C._nn.one_hot}
              142532096 1287.336    0.000 1287.336    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2545216   41.307    0.000 1276.326    0.001 agent.py:172(__call__)
                2545216   41.009    0.000 1177.735    0.000 agent.py:112(__call__)
                7635648  182.560    0.000 1121.530    0.000 optimizer.py:189(zero_grad)
             1286370090 1093.620    0.000 1093.620    0.000 layer.py:154(elements)
                5892942  114.872    0.000 1057.673    0.000 levels.py:164(generate)
             4317401257  738.665    0.000 1056.044    0.000 enum.py:646(__hash__)
              256264305  210.384    0.000  885.374    0.000 {built-in method builtins.any}
              254441789  547.113    0.000  873.797    0.000 layers.py:246(check)
               11648600  308.996    0.000  854.819    0.000 exploration.py:53(softmaxer)
               71266048  833.060    0.000  833.060    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              254441789  472.912    0.000  810.381    0.000 layers.py:286(check)
               11785884  108.132    0.000  789.216    0.000 level.py:41(notUsed)
            10393278797  656.078    0.000  730.956    0.000 {built-in method builtins.len}
               71266048  687.689    0.000  687.689    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              254521600   78.682    0.000  683.346    0.000 {built-in method builtins.all}
             2237657922  549.117    0.000  674.991    0.000 layers.py:809(<genexpr>)
               71266048  671.340    0.000  671.340    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               71266048  660.197    0.000  660.197    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              873555818  228.643    0.000  634.207    0.000 layers.py:799(<genexpr>)
                2545216   45.422    0.000  607.224    0.000 replaybuffer.py:18(stacker)
                2545216   47.855    0.000  602.646    0.000 replaybuffer.py:63(stacker)
              186829049  562.830    0.000  562.830    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                2545216  313.600    0.000  521.839    0.000 collector.py:46(collect)
               71266048  514.209    0.000  514.209    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               35482660  454.941    0.000  454.941    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               16876316  170.479    0.000  446.964    0.000 random.py:315(sample)
               47143536   55.530    0.000  441.250    0.000 layer.py:77(restart)
             4946656671  437.709    0.000  437.709    0.000 layer.py:99(positions)
              498862336  331.351    0.000  409.626    0.000 tensor.py:906(grad)
              254441789  246.306    0.000  389.885    0.000 layers.py:313(check)
              254441789  235.939    0.000  376.765    0.000 layers.py:273(check)
                7635648   11.742    0.000  373.700    0.000 loss.py:527(forward)
                7635648   28.272    0.000  361.957    0.000 functional.py:2898(mse_loss)
               61880212   48.592    0.000  358.346    0.000 flatten.py:39(forward)
               11785884   11.565    0.000  340.651    0.000 level.py:38(elementsIn)
              254441789  223.802    0.000  336.914    0.000 layers.py:48(check)
             4317430408  317.384    0.000  317.384    0.000 {built-in method builtins.hash}
               61880212  309.755    0.000  309.755    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              564593769  206.022    0.000  291.939    0.000 layer.py:138(add)
              268382955  217.461    0.000  289.061    0.000 layer.py:134(remove)
              169118789  195.285    0.000  288.797    0.000 layers.py:113(isDone)
              411334348  288.077    0.000  288.077    0.000 {built-in method torch._C._get_tracing_state}
               81446896  284.044    0.000  284.044    0.000 layer.py:186(<listcomp>)
                5892942  143.792    0.000  282.305    0.000 layers.py:36(reset)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632962: <Causal3_Conver4_3counterfactsNOCRASH_2_1> in cluster <dcc> Done

Job <Causal3_Conver4_3counterfactsNOCRASH_2_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 15:41:03 2021
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun May 16 23:26:17 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May 16 23:26:17 2021
Terminated at Mon May 17 23:22:15 2021
Results reported at Mon May 17 23:22:15 2021

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

    CPU time :                                   86072.89 sec.
    Max Memory :                                 3453 MB
    Average Memory :                             3441.95 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               12931.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86251 sec.
    Turnaround time :                            459672 sec.

The output (if any) is above this job summary.

