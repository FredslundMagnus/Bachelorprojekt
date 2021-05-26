
# Parameters

    Name :                      Diamonds2_convert2-2
    Main :                      CFagent
    Level :                     Levels.Causal5
    Failed actions chance :     0
    Use model :                 False
    Depth :                     1
    Model explore :             100000
    Samples :                   5
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        2000000.0
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
    Cf convert :                2
    Counterfacts :              1
    Topn :                      2
    Random counterfacts :       False
    Num :                       2
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      65870086597 function calls (65575095530 primitive calls) in 86114.75 seconds

##    Ordered by: cumulative time
   List reduced from 505 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86114.751 86114.751 {built-in method builtins.exec}
                      1    4.275    4.275 86114.751 86114.751 <string>:1(<module>)
                      1  342.043  342.043 86110.476 86110.476 main.py:80(CFagent)
                9074862   33.267    0.000 27265.331    0.003 agent.py:29(learn)
                9074862  681.318    0.000 22714.038    0.003 learner.py:42(Qlearn)
                3024954   15.364    0.000 16454.552    0.005 game.py:42(step)
                3024954   19.246    0.000 15727.367    0.005 layers.py:827(step)
        329655004/34665628 1350.708    0.000 12196.472    0.000 module.py:866(_call_impl)
               25590766   72.757    0.000 11468.420    0.000 network.py:28(forward)
               25590766  361.400    0.000 11230.004    0.000 container.py:117(forward)
                3024954  318.050    0.000 10525.903    0.003 agent.py:54(_learn)
                3024954 1158.031    0.000 10093.644    0.003 agent.py:212(counterfact)
                3024954  315.578    0.000 9740.788    0.003 agent.py:204(_learn)
                9074862   82.096    0.000 9629.277    0.001 optimizer.py:84(wrapper)
                9074862   37.733    0.000 9254.527    0.001 grad_mode.py:24(decorate_context)
                3024954  244.919    0.000 9177.968    0.003 layers.py:17(step)
                9074862  266.571    0.000 9129.879    0.001 adam.py:55(step)
              302126923  483.236    0.000 8908.446    0.000 layer.py:106(move)
                9074862 1868.100    0.000 8554.856    0.001 _functional.py:53(adam)
                3024954 4556.846    0.002 8431.558    0.003 replaybuffer.py:28(teleporter_save_data)
                3024954   91.212    0.000 6946.249    0.002 agent.py:117(_learn)
                3024955  424.235    0.000 6506.232    0.002 layers.py:793(update)
                3024954 4157.670    0.001 6355.200    0.002 agent.py:88(interveen)
                8256899  221.027    0.000 5997.061    0.001 agent.py:49(__call__)
              302126923 1199.740    0.000 5712.557    0.000 layers.py:844(check)
                9074862   35.980    0.000 5641.471    0.001 tensor.py:195(backward)
                9074862   34.742    0.000 5604.132    0.001 __init__.py:68(backward)
                9074862 5367.252    0.001 5367.252    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3024954 4105.877    0.001 5112.899    0.002 replaybuffer.py:22(sample_data)
                3024954 4067.190    0.001 5043.189    0.002 replaybuffer.py:67(sample_data)
               47447196 4680.964    0.000 4680.964    0.000 {built-in method tensor}
               40455346   27.641    0.000 4478.055    0.000 game.py:38(board)
               51181532  129.658    0.000 4075.401    0.000 conv.py:398(forward)
               51181532   64.591    0.000 3892.900    0.000 conv.py:390(_conv_forward)
               51181532 3828.309    0.000 3828.309    0.000 {built-in method conv2d}
              278027023 3509.748    0.000 3509.748    0.000 {built-in method clone}
                2209097   49.658    0.000 3402.777    0.002 agent.py:176(choose_action)
               70722390  140.135    0.000 3232.964    0.000 linear.py:93(forward)
               54449181 1767.281    0.000 3146.168    0.000 layer.py:175(NoRock_update)
               70722390   56.104    0.000 3019.924    0.000 functional.py:1737(linear)
               70722390 2949.636    0.000 2949.636    0.000 {built-in method torch._C._nn.linear}
                3024954 1808.185    0.001 2686.355    0.001 agent.py:67(modify)
                4971755   55.915    0.000 2596.427    0.001 layers.py:849(restart)
              302126923  531.075    0.000 2251.967    0.000 layers.py:838(isFree)
                4971755   24.738    0.000 2185.418    0.000 level.py:8(__init__)
                4971755   75.809    0.000 1938.821    0.000 levels.py:249(generate)
               96313156   76.662    0.000 1803.576    0.000 activation.py:713(forward)
               32316530  299.797    0.000 1788.313    0.000 level.py:41(notUsed)
              169397424 1759.567    0.000 1759.567    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                3024954 1305.749    0.000 1751.528    0.001 replaybuffer.py:73(CF_save_data)
               41531393 1745.379    0.000 1745.379    0.000 {built-in method cat}
               96313156   80.088    0.000 1726.914    0.000 functional.py:1364(leaky_relu)
             2698618589 1426.582    0.000 1720.891    0.000 layer.py:103(isFree)
               11281853   76.071    0.000 1640.949    0.000 agent.py:59(modify_board)
               96313156 1629.887    0.000 1629.887    0.000 {built-in method torch._C._nn.leaky_relu}
              169397424 1535.589    0.000 1535.589    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3024954   53.316    0.000 1529.599    0.001 agent.py:172(__call__)
             6406412978 1030.165    0.000 1467.981    0.000 enum.py:646(__hash__)
                3024954   50.416    0.000 1436.148    0.000 agent.py:112(__call__)
                9074862  216.844    0.000 1345.638    0.000 optimizer.py:189(zero_grad)
              300548700  266.788    0.000 1157.797    0.000 {built-in method builtins.any}
               11281853 1048.086    0.000 1048.086    0.000 {built-in method torch._C._nn.one_hot}
               84698712  954.821    0.000  954.821    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             2975237450  735.589    0.000  891.009    0.000 layers.py:809(<genexpr>)
               32316530   23.055    0.000  882.554    0.000 level.py:38(elementsIn)
              292333830  878.465    0.000  878.465    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              302126923  547.986    0.000  847.560    0.000 layers.py:387(check)
               84698712  828.178    0.000  828.178    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              302126923  516.440    0.000  812.477    0.000 layers.py:337(check)
               84698712  796.984    0.000  796.984    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              302126923  497.460    0.000  790.801    0.000 layers.py:375(check)
                3024954   58.205    0.000  787.868    0.000 replaybuffer.py:18(stacker)
               84698712  787.634    0.000  787.634    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              302126923  501.059    0.000  787.537    0.000 layers.py:349(check)
             1070553358  783.138    0.000  783.138    0.000 layer.py:154(elements)
                3024954   58.439    0.000  766.273    0.000 replaybuffer.py:63(stacker)
                2209097  575.941    0.000  653.164    0.000 agent.py:187(convert_values)
                3024954  374.824    0.000  621.950    0.000 collector.py:46(collect)
             7037275248  620.860    0.000  620.860    0.000 layer.py:99(positions)
                8256899  223.045    0.000  618.480    0.000 exploration.py:53(softmaxer)
               84698712  608.310    0.000  608.310    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               32316530  299.741    0.000  582.650    0.000 level.py:39(<listcomp>)
              302495500   68.967    0.000  570.782    0.000 {built-in method builtins.all}
        7502772079/7502772076  487.182    0.000  547.711    0.000 {built-in method builtins.len}
              769530917  184.879    0.000  536.887    0.000 layers.py:799(<genexpr>)
              592891068  413.521    0.000  513.210    0.000 tensor.py:906(grad)
                9074862   12.082    0.000  439.217    0.000 loss.py:527(forward)
             6406447505  437.822    0.000  437.822    0.000 {built-in method builtins.hash}
                9074862   33.552    0.000  427.135    0.000 functional.py:2898(mse_loss)
                6049908  154.200    0.000  417.006    0.000 random.py:315(sample)
              302126923  246.394    0.000  367.480    0.000 layers.py:364(check)
              302126923  234.739    0.000  359.705    0.000 layers.py:326(check)
             1524159534  345.179    0.000  345.179    0.000 level.py:32(inverse)
               44745795   36.193    0.000  341.489    0.000 layer.py:77(restart)
               51181532   34.826    0.000  301.456    0.000 flatten.py:39(forward)
              302126923  204.855    0.000  298.129    0.000 layers.py:23(check)
             1603398420  282.203    0.000  282.203    0.000 enum.py:352(<genexpr>)
                9074862  281.386    0.000  281.386    0.000 {built-in method torch._C._nn.mse_loss}
               32316530  172.095    0.000  276.849    0.000 {built-in method _functools.reduce}
               51181532  266.630    0.000  266.630    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9678087: <Diamonds2_convert2_2> in cluster <dcc> Done

Job <Diamonds2_convert2_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri May 21 19:42:39 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat May 22 19:42:50 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat May 22 19:42:50 2021
Terminated at Sun May 23 19:38:14 2021
Results reported at Sun May 23 19:38:14 2021

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

    CPU time :                                   85894.80 sec.
    Max Memory :                                 8784 MB
    Average Memory :                             5927.19 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7600.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86159 sec.
    Turnaround time :                            172535 sec.

The output (if any) is above this job summary.

