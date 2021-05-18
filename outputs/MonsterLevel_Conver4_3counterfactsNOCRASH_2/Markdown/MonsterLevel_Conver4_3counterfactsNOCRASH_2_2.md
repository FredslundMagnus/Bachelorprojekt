
# Parameters

    Name :                      MonsterLevel_Conver4_3counterfactsNOCRASH_2-2
    Main :                      Load_Cfagent
    Level :                     Levels.MonsterLevel
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
    Num :                       2
    Load name :                 MonsterLevel_Conver4_3counterfactsNOCRASH
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      57230956880 function calls (56926856003 primitive calls) in 86108.79 seconds

##    Ordered by: cumulative time
   List reduced from 430 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86108.788 86108.788 {built-in method builtins.exec}
                      1    4.205    4.205 86108.788 86108.788 <string>:1(<module>)
                      1  236.847  236.847 86104.583 86104.583 main.py:109(Load_Cfagent)
                2019160 4754.000    0.002 24079.305    0.012 agent.py:212(counterfact)
                6057480   23.255    0.000 20164.252    0.003 agent.py:29(learn)
                2019160   10.643    0.000 17729.485    0.009 game.py:42(step)
                2019160   12.561    0.000 17280.622    0.009 layers.py:827(step)
                6057480  494.273    0.000 16864.243    0.003 learner.py:42(Qlearn)
        336170094/32072038 1526.392    0.000 13413.911    0.000 module.py:866(_call_impl)
               26014558   76.037    0.000 12790.865    0.000 network.py:28(forward)
               26014558  395.363    0.000 12532.725    0.000 container.py:117(forward)
                5940235  138.006    0.000 9924.824    0.002 agent.py:176(choose_action)
                2019160  341.997    0.000 9550.573    0.005 layers.py:793(update)
                9978523  284.463    0.000 7809.107    0.001 agent.py:49(__call__)
                2019160  223.070    0.000 7762.940    0.004 agent.py:54(_learn)
                2019160  191.122    0.000 7701.023    0.004 layers.py:17(step)
              199538526  615.224    0.000 7490.318    0.000 layer.py:106(move)
                2019160  223.439    0.000 7220.075    0.004 agent.py:204(_learn)
                6057480   55.544    0.000 7148.076    0.001 optimizer.py:84(wrapper)
                6057480   27.462    0.000 6884.025    0.001 grad_mode.py:24(decorate_context)
                6057480  204.081    0.000 6795.931    0.001 adam.py:55(step)
                6057480 1382.849    0.000 6378.435    0.001 _functional.py:53(adam)
               76732194 6142.047    0.000 6142.047    0.000 {built-in method tensor}
               72278179   51.375    0.000 6041.144    0.000 game.py:38(board)
                2019160 2976.657    0.001 5548.742    0.003 replaybuffer.py:28(teleporter_save_data)
                8651555   74.478    0.000 5330.836    0.001 layers.py:849(restart)
                2019160   64.875    0.000 5143.886    0.003 agent.py:117(_learn)
              199538526  683.910    0.000 5046.964    0.000 layers.py:844(check)
                8651555   35.131    0.000 4582.280    0.001 level.py:8(__init__)
               52029116  121.398    0.000 4409.166    0.000 conv.py:398(forward)
                2019160 2773.213    0.001 4353.188    0.002 agent.py:88(interveen)
                6057480   24.144    0.000 4259.595    0.001 tensor.py:195(backward)
                6057480   25.366    0.000 4234.395    0.001 __init__.py:68(backward)
               52029116   84.100    0.000 4227.689    0.000 conv.py:390(_conv_forward)
                8651555  679.115    0.000 4176.702    0.000 levels.py:428(generate)
               52029116 4143.588    0.000 4143.588    0.000 {built-in method conv2d}
               48459828 2677.896    0.000 4105.960    0.000 layer.py:159(update)
                6057480 4063.110    0.001 4063.110    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2019160 2991.921    0.001 3698.937    0.002 replaybuffer.py:22(sample_data)
                2019160 2988.918    0.001 3681.231    0.002 replaybuffer.py:67(sample_data)
               74005354  163.279    0.000 3664.878    0.000 linear.py:93(forward)
               74005354   66.745    0.000 3415.752    0.000 functional.py:1737(linear)
               74005354 3332.425    0.000 3332.425    0.000 {built-in method torch._C._nn.linear}
              199538526 1661.524    0.000 2921.455    0.000 layers.py:538(check)
               43257775  434.145    0.000 2836.484    0.000 level.py:41(notUsed)
              196361230 2727.386    0.000 2727.386    0.000 {built-in method clone}
                2019160 1882.618    0.001 2670.115    0.001 replaybuffer.py:73(CF_save_data)
                2019160 1507.235    0.001 2146.839    0.001 agent.py:67(modify)
              100019912   92.992    0.000 2051.162    0.000 activation.py:713(forward)
              100019912   87.325    0.000 1958.170    0.000 functional.py:1364(leaky_relu)
                5940235 1639.360    0.000 1943.375    0.000 agent.py:187(convert_values)
               11997683   87.484    0.000 1865.449    0.000 agent.py:59(modify_board)
              100019912 1851.742    0.000 1851.742    0.000 {built-in method torch._C._nn.leaky_relu}
             5652028210 1033.917    0.000 1487.492    0.000 enum.py:646(__hash__)
              202766586  164.210    0.000 1472.347    0.000 {built-in method builtins.any}
               32189283 1418.730    0.000 1418.730    0.000 {built-in method cat}
              199538526  274.833    0.000 1396.260    0.000 layers.py:838(isFree)
               43257775   36.412    0.000 1321.651    0.000 level.py:38(elementsIn)
              113072960 1317.611    0.000 1317.611    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             1373519087  412.130    0.000 1308.585    0.000 layers.py:809(<genexpr>)
               11997683 1181.304    0.000 1181.304    0.000 {built-in method torch._C._nn.one_hot}
              113072960 1157.449    0.000 1157.449    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2019160   37.936    0.000 1121.672    0.001 agent.py:172(__call__)
             1110620996  933.230    0.000 1121.427    0.000 layer.py:103(isFree)
                2019160   37.643    0.000 1032.865    0.001 agent.py:112(__call__)
                6057480  156.757    0.000  975.985    0.000 optimizer.py:189(zero_grad)
               43257775  421.675    0.000  858.627    0.000 level.py:39(<listcomp>)
             1846954033  828.322    0.000  828.322    0.000 layer.py:154(elements)
              196709107  510.238    0.000  812.947    0.000 layers.py:575(isDead)
                9978523  294.919    0.000  806.682    0.000 exploration.py:53(softmaxer)
              199538526  507.022    0.000  714.185    0.000 layers.py:77(check)
              501628739  558.954    0.000  705.628    0.000 layer.py:134(remove)
               56536480  705.583    0.000  705.583    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               52014497  700.088    0.000  700.088    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               47296095  270.936    0.000  699.428    0.000 random.py:315(sample)
              210378073  699.364    0.000  699.364    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             1845570264  693.753    0.000  693.753    0.000 level.py:32(inverse)
               51909330   68.084    0.000  654.892    0.000 layer.py:77(restart)
              201916000   71.146    0.000  630.400    0.000 {built-in method builtins.all}
               56536480  606.849    0.000  606.849    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               56536480  600.334    0.000  600.334    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               56536480  589.860    0.000  589.860    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              657791092  192.107    0.000  586.857    0.000 layers.py:799(<genexpr>)
             6607531244  488.121    0.000  555.270    0.000 {built-in method builtins.len}
                2019160   39.564    0.000  552.260    0.000 replaybuffer.py:18(stacker)
              296820770  108.888    0.000  542.233    0.000 random.py:244(randint)
                2019160   41.906    0.000  541.659    0.000 replaybuffer.py:63(stacker)
              691728964  363.883    0.000  521.657    0.000 random.py:250(_randbelow_with_getrandbits)
              886471232  355.557    0.000  481.323    0.000 layer.py:138(add)
                2019160  278.785    0.000  462.009    0.000 collector.py:46(collect)
                8651555  229.931    0.000  459.127    0.000 layers.py:36(reset)
             5652051537  453.579    0.000  453.579    0.000 {built-in method builtins.hash}
               56536480  448.953    0.000  448.953    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              296820770  182.919    0.000  433.345    0.000 random.py:200(randrange)
             2232101205  430.760    0.000  430.760    0.000 enum.py:352(<genexpr>)
               43257775  264.665    0.000  426.612    0.000 {built-in method _functools.reduce}
             4339540490  422.952    0.000  422.952    0.000 layer.py:99(positions)
              201916000  247.501    0.000  362.467    0.000 layers.py:113(isDone)
              395755360  284.097    0.000  353.149    0.000 tensor.py:906(grad)
                8651555  171.184    0.000  350.500    0.000 level.py:16(<dictcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632960: <MonsterLevel_Conver4_3counterfactsNOCRASH_2_2> in cluster <dcc> Done

Job <MonsterLevel_Conver4_3counterfactsNOCRASH_2_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 15:41:02 2021
Job was executed on host(s) <n-62-20-13>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu May 13 16:57:52 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu May 13 16:57:52 2021
Terminated at Fri May 14 16:53:05 2021
Results reported at Fri May 14 16:53:05 2021

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

    CPU time :                                   85901.56 sec.
    Max Memory :                                 7248 MB
    Average Memory :                             5322.21 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               9136.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86113 sec.
    Turnaround time :                            177123 sec.

The output (if any) is above this job summary.

