
# Parameters

    Name :                      MonsterLevel_Conver4_3counterfactsNOCRASH-0
    Main :                      CFagent
    Level :                     Levels.MonsterLevel
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
    Cf convert :                4
    Counterfacts :              3
    Topn :                      5
    Random counterfacts :       False
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      61080620973 function calls (60734786498 primitive calls) in 86119.10 seconds

##    Ordered by: cumulative time
   List reduced from 509 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86119.099 86119.099 {built-in method builtins.exec}
                      1    4.237    4.237 86119.099 86119.099 <string>:1(<module>)
                      1  263.514  263.514 86114.862 86114.862 main.py:80(CFagent)
                2338327 4250.193    0.002 23779.763    0.010 agent.py:212(counterfact)
                7014981   26.578    0.000 21072.268    0.003 agent.py:29(learn)
                7014981  527.632    0.000 17555.599    0.003 learner.py:42(Qlearn)
                2338327   11.463    0.000 16910.703    0.007 game.py:42(step)
                2338327   14.406    0.000 16415.728    0.007 layers.py:827(step)
        382446606/36613822 1501.122    0.000 13814.325    0.000 module.py:866(_call_impl)
               29598841   80.139    0.000 13168.231    0.000 network.py:28(forward)
               29598841  405.279    0.000 12910.725    0.000 container.py:117(forward)
                6615298  141.010    0.000 10038.102    0.002 agent.py:176(choose_action)
                2338328  340.781    0.000 8466.352    0.004 layers.py:793(update)
                2338327  246.371    0.000 8120.722    0.003 agent.py:54(_learn)
               11291908  301.579    0.000 8051.561    0.001 agent.py:49(__call__)
                2338327  200.352    0.000 7917.403    0.003 layers.py:17(step)
              230474843  626.679    0.000 7695.421    0.000 layer.py:106(move)
                2338327  246.478    0.000 7544.155    0.003 agent.py:204(_learn)
                7014981   59.456    0.000 7426.757    0.001 optimizer.py:84(wrapper)
                7014981   28.406    0.000 7139.159    0.001 grad_mode.py:24(decorate_context)
                7014981  204.810    0.000 7045.108    0.001 adam.py:55(step)
                7014981 1440.659    0.000 6609.193    0.001 _functional.py:53(adam)
               83783287 6531.273    0.000 6531.273    0.000 {built-in method tensor}
               78304810   54.394    0.000 6409.285    0.000 game.py:38(board)
                2338327   72.232    0.000 5366.081    0.002 agent.py:117(_learn)
              230474843  703.774    0.000 5169.564    0.000 layers.py:844(check)
                2338327 2727.580    0.001 5043.315    0.002 replaybuffer.py:28(teleporter_save_data)
                8307735   66.351    0.000 4598.882    0.001 layers.py:849(restart)
               59197682  125.267    0.000 4580.680    0.000 conv.py:398(forward)
               59197682   78.511    0.000 4402.549    0.000 conv.py:390(_conv_forward)
                7014981   27.410    0.000 4385.285    0.001 tensor.py:195(backward)
                7014981   25.836    0.000 4356.763    0.001 __init__.py:68(backward)
               59197682 4324.037    0.000 4324.037    0.000 {built-in method conv2d}
                7014981 4174.985    0.001 4174.985    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2338327 2507.140    0.001 4172.600    0.002 agent.py:88(interveen)
                2338327 3389.558    0.001 4157.260    0.002 replaybuffer.py:22(sample_data)
                2338327 3396.569    0.001 4145.085    0.002 replaybuffer.py:67(sample_data)
               56119842 2580.640    0.000 4032.839    0.000 layer.py:159(update)
                8307735   32.831    0.000 3951.502    0.000 level.py:8(__init__)
               84119869  170.602    0.000 3810.624    0.000 linear.py:93(forward)
                8307735  588.583    0.000 3587.155    0.000 levels.py:428(generate)
               84119869   69.304    0.000 3565.502    0.000 functional.py:1737(linear)
               84119869 3479.374    0.000 3479.374    0.000 {built-in method torch._C._nn.linear}
              230474843 1696.816    0.000 2987.595    0.000 layers.py:538(check)
              193212324 2452.100    0.000 2452.100    0.000 {built-in method clone}
               41538675  372.914    0.000 2431.845    0.000 level.py:41(notUsed)
                2338327 1727.591    0.001 2422.981    0.001 replaybuffer.py:73(CF_save_data)
                2338327 1525.712    0.001 2209.203    0.001 agent.py:67(modify)
              113718710   86.672    0.000 2119.923    0.000 activation.py:713(forward)
              113718710   93.396    0.000 2033.251    0.000 functional.py:1364(leaky_relu)
                6615298 1662.742    0.000 1970.385    0.000 agent.py:187(convert_values)
               13630235   90.799    0.000 1960.426    0.000 agent.py:59(modify_board)
              113718710 1919.151    0.000 1919.151    0.000 {built-in method torch._C._nn.leaky_relu}
               37013505 1530.765    0.000 1530.765    0.000 {built-in method cat}
              238028888  167.932    0.000 1510.261    0.000 {built-in method builtins.any}
              230474843  283.978    0.000 1453.333    0.000 layers.py:838(isFree)
              130946312 1359.225    0.000 1359.225    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             1611608513  441.895    0.000 1342.962    0.000 layers.py:809(<genexpr>)
             5669589981  912.180    0.000 1317.297    0.000 enum.py:646(__hash__)
               13630235 1248.491    0.000 1248.491    0.000 {built-in method torch._C._nn.one_hot}
              130946312 1189.293    0.000 1189.293    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2338327   43.463    0.000 1184.234    0.001 agent.py:172(__call__)
             1321102932  983.783    0.000 1169.354    0.000 layer.py:103(isFree)
               41538675   32.358    0.000 1131.555    0.000 level.py:38(elementsIn)
                2338327   40.981    0.000 1113.299    0.000 agent.py:112(__call__)
                7014981  162.573    0.000 1026.298    0.000 optimizer.py:189(zero_grad)
             1928308591  835.826    0.000  835.826    0.000 layer.py:154(elements)
               11291908  302.458    0.000  834.444    0.000 exploration.py:53(softmaxer)
              231013908  509.627    0.000  819.130    0.000 layers.py:575(isDead)
               65473156  738.188    0.000  738.188    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               41538675  371.102    0.000  735.883    0.000 level.py:39(<listcomp>)
              230474843  514.740    0.000  719.487    0.000 layers.py:77(check)
               46215329  255.997    0.000  659.724    0.000 random.py:315(sample)
               65473156  640.173    0.000  640.173    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              209180886  632.769    0.000  632.769    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               49965473  623.054    0.000  623.054    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               65473156  617.418    0.000  617.418    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                2338327   41.845    0.000  605.456    0.000 replaybuffer.py:18(stacker)
               65473156  604.496    0.000  604.496    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              541477956  453.025    0.000  596.830    0.000 layer.py:134(remove)
             1772214522  593.973    0.000  593.973    0.000 level.py:32(inverse)
                2338327   43.409    0.000  591.118    0.000 replaybuffer.py:63(stacker)
        7592558415/7592558412  502.349    0.000  571.738    0.000 {built-in method builtins.len}
               49846410   56.177    0.000  565.212    0.000 layer.py:77(restart)
              331114095  103.036    0.000  538.033    0.000 random.py:244(randint)
              750281176  350.733    0.000  504.417    0.000 random.py:250(_randbelow_with_getrandbits)
                2338327  288.913    0.000  480.257    0.000 collector.py:46(collect)
               65473156  474.372    0.000  474.372    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              918355646  339.878    0.000  458.632    0.000 layer.py:138(add)
              331114095  182.623    0.000  434.997    0.000 random.py:200(randrange)
             4615758710  409.987    0.000  409.987    0.000 layer.py:99(positions)
             5669616780  405.122    0.000  405.122    0.000 {built-in method builtins.hash}
                8307835  199.272    0.000  395.402    0.000 layers.py:36(reset)
              458312176  305.530    0.000  378.888    0.000 tensor.py:906(grad)
             2143397666  376.092    0.000  376.092    0.000 enum.py:352(<genexpr>)
               41538675  224.972    0.000  363.314    0.000 {built-in method _functools.reduce}
              230474843  242.257    0.000  353.719    0.000 layers.py:48(check)
               59197682   40.480    0.000  344.624    0.000 flatten.py:39(forward)
                7014981    9.343    0.000  340.517    0.000 loss.py:527(forward)
              230474843  118.637    0.000  337.735    0.000 layers.py:572(<listcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9624184: <MonsterLevel_Conver4_3counterfactsNOCRASH_0> in cluster <dcc> Done

Job <MonsterLevel_Conver4_3counterfactsNOCRASH_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun May  9 01:29:17 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon May 10 02:21:52 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May 10 02:21:52 2021
Terminated at Tue May 11 02:17:23 2021
Results reported at Tue May 11 02:17:23 2021

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

    CPU time :                                   85900.54 sec.
    Max Memory :                                 7860 MB
    Average Memory :                             5672.44 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8524.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86132 sec.
    Turnaround time :                            175686 sec.

The output (if any) is above this job summary.

